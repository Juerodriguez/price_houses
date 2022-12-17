import dataclasses
from typing import Iterable


@dataclasses.dataclass
class Price:
    value: str


@dataclasses.dataclass
class Location:
    localidad: str
    provincia: str
    region: str


@dataclasses.dataclass
class House:
    price: Price
    location: Location


@dataclasses.dataclass
class HousesResult:
    houses: list
