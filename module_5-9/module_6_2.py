class Vehicle:
    _COLOR_VARIANTS = ['ultramarine', 'indigo', 'lime', 'cyan', 'crimson']

    def __init__(self, owner: str, __model: str,__color: str,  __engine_power: int):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color

    def get_model(self):
        return f'Модель: {self.model}'

    def get_engine_power(self):
        return f'Мощность двигателя: {self.engine_power}'

    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_engine_power())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        for color in self._COLOR_VARIANTS:
             if new_color.lower() == color.lower():
                self.color = new_color
                return True
        print(f"Нельзя сменить цвет на {new_color}")
        return False


class Sedan(Vehicle):
    def __init__(self,owner: str, __model: str, __engine_power: int, __color: str, __PASSENGERS_LIMIT = 5):
        super().__init__(owner, __model, __engine_power, __color)
        self.__PASSENGERS_LIMIT = __PASSENGERS_LIMIT


if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['ultramarine', 'indigo', 'lime', 'cyan', 'crimson']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'ultramarine', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('CyAn')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()
