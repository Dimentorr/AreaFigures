import math


class FigureWithAngle:
    def __init__(self, *sides):
        self.sides = list(sides)

    def get_perimeter(self):
        return sum(self.sides)


class Circle:
    def __init__(self, radius):
        self.Pi = 3.14
        if type(radius) == int or type(radius) == float and radius > 0:
            self.radius = radius
        else:
            self.radius = -1

    def get_area(self):
        if self.radius > 0:
            return 2 * self.radius * self.Pi
        else:
            return 'Incorrect data'


class Triangle(FigureWithAngle):
    def __init__(self, *sides):
        super().__init__(*sides)
        self.check = ''
        try:
            self.more_side, self.cathets = self.determining_sides()
        except TypeError:
            self.more_side, self.cathets = 0, (0, 0)
            raise Exception(self.check)

    @staticmethod
    def check_data(sides):
        if any([type(i) == str for i in sides]):
            return 'Incorrect data. Was input string.'
        elif any(i <= 0 for i in sides):
            return 'Incorrect data. Impossible value.'
        else:
            return 1

    def get_area_by_three_sides(self):
        self.check = self.check_data(self.sides)
        if self.check == 1:
            p = self.get_perimeter() / 2
            tmp_answer = p * (p - self.more_side) * (p - self.cathets[0]) * (p - self.cathets[1])
            try:
                return round(math.sqrt(tmp_answer), 2)
            except ValueError:
                raise Exception('Incorrect triangle aspect ratio.')
        else:
            raise Exception(self.check)

    def react_triangle(self):
        self.check = self.check_data(self.sides)
        if self.check == 1:
            flag = sum([i ** 2 for i in self.cathets]) == self.more_side ** 2
            return flag
        else:
            raise Exception(self.check)

    def determining_sides(self):
        cathets = list()
        more_side = 0
        try:
            for i in self.sides:
                if i > more_side & more_side != 0:
                    cathets.append(more_side)
                    more_side = i
                elif i > more_side:
                    more_side = i
                else:
                    cathets.append(i)
            return more_side, cathets
        except TypeError:
            return 0, 0


def find_area(*args):
    if len(args) == 1:
        figure = Circle(args[0])
        return figure.get_area()
    elif len(args) == 3:
        figure = Triangle(list(args))
        return figure.get_area_by_three_sides()
    else:
        return 'I dont now this figure'