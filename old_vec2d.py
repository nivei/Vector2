from __future__ import annotations
from typing import Union
import math
import random


class Vec2d:
    def __init__(self, x: float, y: float):
        self.xy = [x, y]

    def __add__(self, other: Union[float, Vec2d]) -> Vec2d:
        if isinstance(other, self.__class__):
            return Vec2d(self.xy[0] + other.xy[0], self.xy[1] + other.xy[1])
        return Vec2d(self.xy[0] + other, self.xy[1] + other)

    def __sub__(self, other: Union[float, Vec2d]) -> Vec2d:
        if isinstance(other, self.__class__):
            return Vec2d(self.xy[0] - other.xy[0], self.xy[1] - other.xy[1])
        return Vec2d(self.xy[0] - other, self.xy[1] - other)

    def __mul__(self, other: Union[float, Vec2d]) -> Vec2d:
        if isinstance(other, self.__class__):
            return Vec2d(self.xy[0] * other.xy[0], self.xy[1] * other.xy[1])
        return Vec2d(self.xy[0] * other, self.xy[1] * other)

    def __rmul__(self, other: Union[float, Vec2d]) -> Vec2d:
        return self.__mul__(other)

    def __truediv__(self, other: Union[float, Vec2d]) -> Vec2d:
        if isinstance(other, self.__class__):
            if other.xy[0] != 0 and other.xy[1] != 0:
                return Vec2d(self.xy[0] / other.xy[0], self.xy[1] / other.xy[1])
        if other.xy[0] != 0 and other.xy[1] != 0:
            return Vec2d(self.xy[0] / other, self.xy[1] / other)
        return Vec2d(0, 0)

    def __eq__(self, other: Union[float, Vec2d]) -> bool:
        if isinstance(other, self.__class__):
            return self.xy[0] == other.xy[0] and self.xy[1] == other.xy[1]
        return self.xy[0] == other and self.xy[1] == other

    def __neg__(self) -> Vec2d:
        return Vec2d(-self.xy[0], -self.xy[1])

    def length_sqr(self) -> float:
        return self.xy[0] ** 2 + self.xy[1] ** 2

    def length(self) -> float:
        return math.sqrt(self.length_sqr())

    def dist_sqr(self, vec: Vec2d) -> float:
        v = self - vec
        return v.length_sqr()

    def dist(self, vec: Vec2d) -> float:
        v = self - vec
        return v.length()

    def rotate(self, angle: float) -> None:
        cash_x = self.xy[0]
        cs = math.cos(angle)
        sn = math.sin(angle)
        self.xy[0] = cs * cash_x - sn * self.xy[1]
        self.xy[1] = sn * cash_x + cs * self.xy[1]

    def normalize(self) -> None:
        vec_length = self.length()

        if vec_length < 0.00001:
            self.xy = [0, 1]

        else:
            self.xy = [self.xy[0] / vec_length, self.xy[1] / vec_length]

    def scale_to_length(self, length: float) -> None:
        self.normalize()
        self *= length

    def make_int_tuple(self) -> tuple[int, int]:
        return int(self.xy[0]), int(self.xy[1])

    def set(self, vec: Vec2d) -> None:
        self.xy[0] = vec.xy[0]
        self.xy[1] = vec.xy[1]


def dot(vec1: Vec2d, vec2: Vec2d) -> float:
    return vec1.xy[0] * vec2.xy[0] + vec1.xy[1] * vec2.xy[1]


def angle_between(vec1: Vec2d, vec2: Vec2d) -> float:
    return math.acos(dot(vec1, vec2))


def right(vec: Vec2d) -> Vec2d:
    return Vec2d(-vec.xy[1], vec.xy[0])


def left(vec: Vec2d) -> Vec2d:
    return -right(vec)


def random_vector() -> Vec2d:
    return Vec2d(random.random() * 2.0 - 1.0, random.random() * 2.0 - 1.0)


def vector_from_angle(angle: float) -> Vec2d:
    return Vec2d(math.cos(angle), math.sin(angle))


def random_direction() -> Vec2d:
    vec = random_vector()
    vec.normalize()
    return vec


def copy(vec: Vec2d) -> Vec2d:
    return Vec2d(vec.xy[0], vec.xy[1])
