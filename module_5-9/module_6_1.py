class Plant:
    def __init__(self, name=None, edible=False):
        self.name = name
        self.edible = edible


class Animal:
    def __init__(self, name=None):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food: Plant):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name=None):
        super().__init__(name)
        self.edible = True


if __name__ == "__main__":
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

    # Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
