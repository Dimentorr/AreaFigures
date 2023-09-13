import math


class FigureWithAngle:
    def __init__(self, *sides):
        self.sides = list(sides[0])

    def get_perimeter(self):
        return sum(self.sides)


class Circle:
    def __init__(self, radius):
        self.Pi = 3.14
        if radius < 0:
            print('Incorrect data')
            self.radius = 0
        else:
            self.radius = radius

    def get_area(self):
        try:
            return 2 * self.radius * self.Pi
        except():
            return 0


class Triangle(FigureWithAngle):
    def __init__(self, *sides):
        super().__init__(*sides)
        if any(x > 0 for x in self.sides):
            print('Incorrect data')
        self.more_side, self.cathets = self.determining_sides()

    def get_area_by_three_sides(self):
        p = self.get_perimeter() / 2
        tmp_answer = p * (p - self.more_side) * (p - self.cathets[0]) * (p - self.cathets[1])
        try:
            return math.sqrt(tmp_answer)
        except ValueError:
            print('Incorrect triangle aspect ratio')
            return 0

    def react_triangle(self):
        flag = sum([i ** 2 for i in self.cathets]) == self.more_side ** 2
        return flag

    def determining_sides(self):
        cathets = list()
        more_side = 0
        for i in self.sides:
            if i > more_side & more_side != 0:
                cathets.append(more_side)
                more_side = i
            elif i > more_side:
                more_side = i
            else:
                cathets.append(i)
        return more_side, cathets


def find_area(*args):
    if len(args) == 1:
        figure = Circle(args[0])
        return figure.get_area()
    elif len(args) == 3:
        figure = Triangle(list(args))
        return figure.get_area_by_three_sides()
    else:
        return 'I dont now this figure'
