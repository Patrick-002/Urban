import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        cls = type(self)  # Получение текущего класса
        sides_count = cls.sides_count  # определение текущего sides_count для корректной работы
        if len(sides) != sides_count:
            self.__sides = [1] * cls.sides_count
        else:
            self.__sides = list(sides)
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.filled and self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        cls = type(self)
        sides_count = cls.sides_count
        if len(sides) != sides_count:
            return False
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        self.__radius = sides[0] / 2 * math.pi
        super().__init__(color, *sides)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        per = len(self)
        return math.sqrt(per * (per - self.__sides[0]) * (per - self.__sides[1]) * (per - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        sides = sides * 12
        super().__init__(color, *sides)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
    # проверка на единичную сторону
    cube2 = Cube((222, 35, 130), 6, 6)
    print(cube2.get_sides())