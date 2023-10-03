from __future__ import annotations
from typing import Union
import math
import random


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f'Vector<{self.x}, {self.y}> object at {hex(id(self))}'

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, val: float) -> None:
        self.__x = val

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, val: float) -> None:
        self.__y = val

    @property
    def xy(self) -> tuple:
        return self.__x, self.__y

    @xy.setter
    def xy(self, other: Union[Vector, iter, float]) -> None:
        if isinstance(other, self.__class__):
            self.__x = other.x
            self.__y = other.y
        elif hasattr(other, '__iter__'):
            self.__x = other[0]
            self.__y = other[1]
        else:
            self.__x = other
            self.__y = other

    def __add__(self, other: Union[float, Vector]) -> Vector:
        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other, self.y + other)

    def __sub__(self, other: Union[float, Vector]) -> Vector:
        if isinstance(other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other, self.y - other)

    def __mul__(self, other: Union[float, Vector]) -> Vector:
        if isinstance(other, self.__class__):
            return Vector(self.x * other.x, self.y * other.y)
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other: Union[float, Vector]) -> Vector:
        return self.__mul__(other)

    def __truediv__(self, other: Union[float, Vector]) -> Vector:
        if isinstance(other, self.__class__):
            if other.x != 0 and other.y != 0:
                return Vector(self.x / other.x, self.y / other.y)
        if other.x != 0 and other.y != 0:
            return Vector(self.x / other, self.y / other)
        return Vector(0, 0)

    def __eq__(self, other: Union[float, Vector]) -> bool:
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return self.x == other and self.y == other

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y)

    def length_sqr(self) -> float:
        return self.x ** 2 + self.y ** 2

    def length(self) -> float:
        return math.sqrt(self.length_sqr())

    def distance_sqr(self, vec: Vector) -> float:
        v = self - vec
        return v.length_sqr()

    def distance(self, vec: Vector) -> float:
        v = self - vec
        return v.length()

    def rotate(self, angle: float) -> None:
        cash_x = self.x
        cs = math.cos(math.radians(angle))
        sn = math.sin(math.radians(angle))
        self.x = cs * cash_x - sn * self.y
        self.y = sn * cash_x + cs * self.y

    def rotate_rad(self, angle: float) -> None:
        cash_x = self.x
        cs = math.cos(angle)
        sn = math.sin(angle)
        self.x = cs * cash_x - sn * self.y
        self.y = sn * cash_x + cs * self.y

    def normalize(self) -> None:
        vec_length = self.length()

        if vec_length < 0.00001:
            self.xy = 0, 1
        else:
            self.xy = self.x / vec_length, self.y / vec_length

    def normalize_ip(self) -> Vector:
        vec_length = self.length()

        if vec_length < 0.00001:
            return Vector(0, 1)
        return Vector(self.x / vec_length, self.y / vec_length)

    def scale_to_length(self, length: float) -> None:
        self.normalize()
        self.x *= length
        self.y *= length

    def make_int_tuple(self) -> tuple[int, int]:
        return int(self.x), int(self.y)

    def set(self, vec: Vector) -> None:
        self.x = vec.x
        self.y = vec.y


def dot(vec1: Vector, vec2: Vector) -> float:
    return vec1.x * vec2.x + vec1.y * vec2.y


def angle_between(vec1: Vector, vec2: Vector) -> float:
    return math.acos(dot(vec1, vec2))


def right(vec: Vector) -> Vector:
    return Vector(-vec.y, vec.x)


def left(vec: Vector) -> Vector:
    return -right(vec)


def random_vector() -> Vector:
    return Vector(random.random() * 2.0 - 1.0, random.random() * 2.0 - 1.0)


def vector_from_angle(angle: float) -> Vector:
    return Vector(math.cos(angle), math.sin(angle))


def random_direction() -> Vector:
    vec = random_vector()
    vec.normalize()
    return vec


def copy(vec: Vector) -> Vector:
    return Vector(vec.x, vec.y)
