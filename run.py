import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from entities import House, HousesResult


BROWSER = webdriver.Firefox()
BROWSER.implicitly_wait(5)


def run_searcher():
    houses_list = []
    BROWSER.get('https://inmuebles.mercadolibre.com.ar/departamentos/alquiler/#filter')
    sleep(2)
    while True:
        html_source = BROWSER.page_source
        soup = BeautifulSoup(html_source, 'lxml')
        soup_list = soup.findAll("li", class_="ui-search-layout__item")
        for soup_element in soup_list:
            prices = soup_element.find(class_="price-tag-fraction").text.replace(".", "")
            locations = soup_element.find(class_="ui-search-item__location").text.split(",")
            size = soup_element\
                .find(class_="ui-search-card-attributes ui-search-item__group__element shops__items-group-details")\
                .text.split(" ")

            obj_house = House(prices, locations[-1], size[0])
            houses_list.append(obj_house.__dict__)

        try:
            soup_list = soup.findAll("li", class_="andes-pagination__button andes-pagination__button--next shops__pagination-button")
            href_next_page = soup_list[0].find(class_="andes-pagination__link shops__pagination-link ui-search-link")["href"]
            BROWSER.get(href_next_page)
            sleep(5)
        except:
            break

    with open("houses.json", "w") as archivo:
        json.dump(HousesResult(houses_list).__dict__, archivo, indent=4)


def main():
    run_searcher()
    BROWSER.close()


if __name__ == "__main__":
    main()
