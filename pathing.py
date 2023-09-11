from dataclasses import dataclass
from typing import Iterable, Union, NewType

PointId = int

@dataclass
class Point:
    x: int
    y: int
    floor: int
    linked: Iterable[PointId]

@dataclass
class Coordinates:
    x: int
    y: int

Floor = NewType("Floor", int)

TransitionType = Union[Floor, Coordinates]

@dataclass
class Transition()

points = {
    PointId(1): Point(
        x=100,
        y=100,
        floor=1,
        linked=[2],
    ),
    PointId(2): Point(
        x=300,
        y=200,
        floor=1,
        linked=[1],
    ),
}

names = {
    "Аудитория 1": PointId(1),
}
