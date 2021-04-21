import math
import random

class Vector2:
    def __init__(self, x: float, y: float):
        self.xy = [x, y]

    # Vector operator overloads
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector2(self.xy[0] + other.xy[0], self.xy[1] + other.xy[1])
        return Vector2(self.xy[0] + other, self.xy[1] + other)
            
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vector2(self.xy[0] - other.xy[0], self.xy[1] - other.xy[1])
        return Vector2(self.xy[0] - other, self.xy[1] - other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vector2(self.xy[0] * other.xy[0], self.xy[1] * other.xy[1])
        return Vector2(self.xy[0] * other, self.xy[1] * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            if other.xy[0] != 0 and other.xy[1] != 0:
                return Vector2(self.xy[0] / other.xy[0], self.xy[1] / other.xy[1])
        if other.xy[0] != 0 and other.xy[1] != 0:
            return Vector2(self.xy[0] / other, self.xy[1] / other)
        return Vector2(0, 0)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.xy[0] == other.xy[0] and self.xy[1] == other.xy[1]
        return self.xy[0] == other and self.xy[1] == other

    def __neg__(self):
        return Vector2(-self.xy[0], -self.xy[1])

    def length_sqr(self):
        return self.xy[0] ** 2 + self.xy[1] ** 2

    def length(self):
        return math.sqrt(length_sqr(self))

    def dist_sqr(self, vec):
        return length_sqr(self, vec)

    def dist(self, vec):
        return length(self, vec)

    def normalize(self):
        vec_length = length(self)

        if vec_length < 0.00001:
            self.xy = [0, 1]
            
        else:
            self.xy = [self.xy[0] / vec_length, self.xy[1] / vec_length]

    def make_int_tuple(self):
        return int(self.xy[0]), int(self.xy[1])

    def set(self, vec):
        self.xy[0] = vec.xy[0]
        self.xy[1] = vec.xy[1]

def dot(vec1, vec2):
    return vec1.xy[0] * vec2.xy[0] + vec1.xy[1] * vec2.xy[1]

def angle_between(vec1, vec2):
    return math.acos(dot(vec1, vec2))

def right(vec):
    return Vector2(-vec.xy[1], vec.xy[0])

def left(vec):
    return -right(vec)

def reflect(incident, normal):
    return incident - dot(normal, incident)* 2.0 * normal

def random_vector():
    return Vector2(random.random()* 2.0 - 1.0, random.random()* 2.0 - 1.0)

def random_direction():
    return random_vector().normalize()

def copy(vec):
    return Vector2(vec.xy[0], vec.xy[1])
