class Vehical :
    owner = str
    __model = str
    __engine_power = int
    __color = str

    def __init__(self,owner,__model,__engine_power,__color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f'название модели авто : {self.__model}'

    def get_horsepower(self):
        return f'мощность двигателя в лошадиных силах : {self.__engine_power}'

    def get_color(self):
        return f'Цвет : {self.__color}'

    def print_info(self):
        return f'{self.get_model()},{self.get_horsepower()},{self.get_color()},Владелец : {self.owner}'

    def set_color(self,new_color):
        if isinstance(new_color,str) and new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Некорректный цвет {new_color}')
            print(f'Доступные цвета:')
            for color in self.__COLOR_VARIANTS:
                print(f'\t{color}')


class Sedan(Vehical):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
print(vehicle1)
# Изначальные свойства
vehicle1.print_info()
print(vehicle1.print_info())

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'
print(vehicle1.owner)


# Проверяем что поменялось
vehicle1.print_info()
print(vehicle1.print_info())
