from dataclasses import dataclass
import os
from typing import List
from PIL import Image
import json

PointId = str
PlaneId = str

@dataclass
class Point:
    x: int
    y: int
    floor: int
    linked: List[PointId]
    plane: PlaneId

@dataclass
class Plane:
    background: Image.Image
    foreground: Image.Image

def open_image(file_name):
    return Image.open(os.path.join("resources/images", file_name))

planes = {
    id_: Plane(
        background=open_image(contents["background"]),
        foreground=open_image(contents["foreground"]),
    )
    for id_, contents in json.load(open("resources/planes.json", encoding="utf-8"))
}

points = {
    id_: Point(**contents)
    for id_, contents in json.load(open("resources/points.json", encoding="utf-8"))
}
