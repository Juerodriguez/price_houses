import dataclasses


@dataclasses.dataclass
class House:
    price: str
    location: str
    size: str


@dataclasses.dataclass
class HousesResult:
    houses: list
