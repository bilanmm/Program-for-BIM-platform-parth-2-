# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Iphone:

    def __init__(self, model: str, number: int):
        if not isinstance(model, (str)):
            raise TypeError("Название телефона должно быть типа str")
        self.model = model

        if not isinstance(number, (int)):
            raise TypeError ("Число телефона должно быть типом int")
        if number <= 0:
            raise ValueError ("Число должно быть положительным")
        self.number = number

    def model_param (self, year: int):
        self.year = year

    def number_param (self, battary: int):
        self.battary = battary

apple = Iphone("Iphone", 15)
apple.model_param(2023)
apple.number_param(100)
print(apple.model, apple.number, apple.year, apple.battary)




class Car:

    def __init__(self, model_car: str, year_car: int):  #Модель и год выпуска машины
        if not isinstance(model_car, (str)): #Показывает модель машины
            raise TypeError ("Модель машины должна быть типом данных str")
        self.model_car = model_car

        if not isinstance(year_car, (int)): #Показывает год машины
            raise TypeError ("Год машины должен быть типом данных int")
        if year_car <= 0:
            raise ValueError ("Год машины должен быть положительным значением")
        self.yaer_car = year_car


    def front_back_car(self, year_car) -> bool: #Показывает старая машина или новая
        if year_car in range(2000, 2010):
            return "Машина старого года"
        if year_car in range(2011, 2020):
            return "Машина нового года"
        self.front_back_car = self.year_car

    def country_car(self): #Указывает из какой страны машина
        countries = {
            "BMW": "Германия"
        }
        return countries.get(self.model_car)
        self.country_car = self.model_car

new_car = Car("BMW", 2008)
print("Модель машины:", new_car.model_car, ",", "Год выпуска:", new_car.yaer_car)
print("Возраст машины:", new_car.front_back_car(2015))
print("Страна производителя:", new_car.country_car())


class Univer:   #Класс российский сериал "Универ"
    def __init__(self, look_series: int, full_series: int): #Число посмотренных серий и их полное количество
        if not isinstance(look_series, (int)):
            raise TypeError("Просмотренные серии должны быть типом данных int")
        if look_series <= 0:
            raise ValueError("Кол-во серий не должно быть отрицательным")
        self.look_series = look_series

        if not isinstance(full_series, (int)):
            raise TypeError("Полное количество серий должно быть типом данных int")
        if full_series > 100:
            raise ValueError("Количество серий не может быть больше 100")
        if full_series < 100:
            raise ValueError("Количество серий не может быть меньше 0")
        self.full_series = full_series

    def love_person(self): #Любимый персонаж из сериала
        if self.look_series in range (0, 25):
            return "Гоша"
        self.love_person = self.look_series

        if self.look_series in range (25, 50):
            return "Кузя"
        self.love_person = self.look_series

        if self.look_series in range (50, 100):
            return "Майкл"
        self.love_person = self.look_series

    def love_moment(self): #Любимый момент из сериала
        if 0 <= self.look_series < 25:
            return "Гоша уходит в армию из-за не сданной сесии"
        elif 25 <= self.look_series < 50:
            return "Кузя поет песню шняга шняжная"
        elif 50 <= self.look_series < 100:
            return "Майкл пытается заплакать"
        self.love_moment = self.love_person

ser = Univer(45,100)
print("Количество серий в сезоне:", ser.full_series)
print("Посмотрено серий:", ser.look_series)
print("Любимый персонаж:", ser.love_person())
print("Любимый момент:", ser.love_moment())

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
