from dataclasses import dataclass
from typing import Iterable

PointId = str

@dataclass
class Point:
    x: int
    y: int
    floor: int
    linked: Iterable[PointId]

points = {
    "Name": Point(
        x=100,
        y=100,
        floor=1,
        linked=["Name2"],
    ),
    "Name2": Point(
        x=300,
        y=200,
        floor=1,
        linked=["Name"],
    ),
}
