"""
Модуль с классами автомобилей.
"""

class Car:
    """
    Базовый класс автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int, max_speed: float) -> None:
        """
        Конструктор автомобиля.

        :param brand: Марка
        :param model: Модель
        :param year: Год выпуска
        :param max_speed: Максимальная скорость
        """
        self._brand = brand        # делаем защищёнными, чтобы нельзя было просто так поменять
        self._model = model
        self._year = year
        self._max_speed = max_speed

    # Геттеры для неизменяемых атрибутов
    def get_brand(self) -> str:
        """Возвращает марку."""
        return self._brand

    def get_model(self) -> str:
        """Возвращает модель."""
        return self._model

    # Свойства для изменяемых атрибутов (с простой проверкой)
    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        if value < 1886 or value > 2030:
            raise ValueError("Год должен быть от 1886 до 2030")
        self._year = value

    @property
    def max_speed(self) -> float:
        return self._max_speed

    @max_speed.setter
    def max_speed(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Скорость должна быть положительной")
        self._max_speed = value

    def info(self) -> str:
        """Возвращает информацию об автомобиле."""
        return f"{self._brand} {self._model}, {self._year} год, макс. скорость {self._max_speed} км/ч"

    def start_engine(self) -> str:
        """Запускает двигатель."""
        return "Двигатель запущен"

    def __str__(self) -> str:
        return f"{self._brand} {self._model}"

    def __repr__(self) -> str:
        return f"Car('{self._brand}', '{self._model}', {self._year}, {self._max_speed})"


class PassengerCar(Car):
    """
    Легковой автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, max_speed: float, doors: int) -> None:
        """
        Конструктор легкового автомобиля.
        """
        super().__init__(brand, model, year, max_speed)
        self._doors = doors

    @property
    def doors(self) -> int:
        return self._doors

    @doors.setter
    def doors(self, value: int) -> None:
        if value not in (2, 3, 4, 5):
            raise ValueError("Количество дверей должно быть 2, 3, 4 или 5")
        self._doors = value

    def info(self) -> str:
        """Переопределяем метод info, добавляя количество дверей."""
        base_info = super().info()
        return base_info + f", дверей: {self._doors}"

    def __repr__(self) -> str:
        return f"PassengerCar('{self.get_brand()}', '{self.get_model()}', {self.year}, {self.max_speed}, {self.doors})"


class Truck(Car):
    """
    Грузовой автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, max_speed: float, load_capacity: float) -> None:
        """
        Конструктор грузового автомобиля.
        """
        super().__init__(brand, model, year, max_speed)
        self._load_capacity = load_capacity

    @property
    def load_capacity(self) -> float:
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Грузоподъёмность должна быть положительной")
        self._load_capacity = value

    def info(self) -> str:
        """Переопределяем метод info, добавляя грузоподъёмность."""
        base_info = super().info()
        return base_info + f", грузоподъёмность: {self._load_capacity} т"

    def __repr__(self) -> str:
        return f"Truck('{self.get_brand()}', '{self.get_model()}', {self.year}, {self.max_speed}, {self.load_capacity})"


if __name__ == "__main__":
    #проверка
    car1 = PassengerCar("Toyota", "Camry", 2020, 220, 4)
    car2 = Truck("Volvo", "FH", 2019, 150, 20.5)

    print(car1)
    print(car1.info())
    print(car1.start_engine())
    print(repr(car1))

    print("\n---\n")

    print(car2)
    print(car2.info())
    print(car2.start_engine())
    print(repr(car2))
