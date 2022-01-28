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
        return math.sqrt(self.length_sqr())

    def dist_sqr(self, vec):
        v = self - vec
        return v.length_sqr()

    def dist(self, vec):
        v = self - vec
        return v.length()
    
    def rotate(self, angle):
        cash_x = self.xy[0]
        cs = math.cos(angle)
        sn = math.sin(angle)
        self.xy[0] = cs * cash_x - sn * self.xy[1]
        self.xy[1] = sn * cash_x + cs * self.xy[1]

    def normalize(self):
        vec_length = self.length()

        if vec_length < 0.00001:
            self.xy = [0, 1]
            
        else:
            self.xy = [self.xy[0] / vec_length, self.xy[1] / vec_length]

    def scale_to_length(self, length):
        self.normalize()
        self *= length

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

def vector_from_angle(angle):
    return Vector2(math.cos(angle), math.sin(angle))

def random_direction():
    return random_vector().normalize()

def copy(vec):
    return Vector2(vec.xy[0], vec.xy[1])
