# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Iphone:
    """
    Класс для представления iPhone.

    Атрибуты:
        model (str): модель телефона
        number (int): номер телефона (целое положительное число)
        year (int): год выпуска (устанавливается методом model_param)
        battery (int): ёмкость аккумулятора (устанавливается методом number_param)

    """

    def __init__(self, model: str, number: int) -> None:
        """
        Инициализация объекта iPhone.

        :param model: модель телефона (строка)
        :param number: номер телефона (целое положительное число)

        """
        if not isinstance(model, str):
            raise TypeError("Название телефона должно быть типа str")
        self.model = model

        if not isinstance(number, int):
            raise TypeError("Номер телефона должен быть типом int")
        if number <= 0:
            raise ValueError("Номер должен быть положительным")
        self.number = number

    def model_param(self, year: int) -> None:
        """
        Устанавливает год выпуска телефона.

        :param year: год выпуска (целое число)

        """
        self.year = year

    def number_param(self, battery: int) -> None:
        """
        Устанавливает ёмкость аккумулятора.

        :param battery: ёмкость аккумулятора (целое число)

        """

        self.battery = battery


class Car:
    """
    Класс для представления автомобиля.

    Примеры использования:
    >>> car1 = Car("BMW", 2008)
    >>> car1.model
    'BMW'
    >>> car1.year
    2008
    >>> car1.age_category()
    'старая'
    >>> car1.country()
    'Германия'

    >>> car2 = Car("Toyota", 2015)
    >>> car2.age_category()
    'новая'
    >>> car2.country()
    'Неизвестно'
    """

    def __init__(self, model: str, year: int) -> None:
        """
        Инициализация автомобиля.

        :param model: марка автомобиля (строка)
        :param year: год выпуска (целое положительное число)

        >>> car = Car("Audi", 2020)
        >>> car.model
        'Audi'
        >>> car.year
        2020
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        self.model = model

        if not isinstance(year, int):
            raise TypeError("Год должен быть целым числом")
        if year <= 0:
            raise ValueError("Год должен быть положительным")
        self.year = year

    def age_category(self) -> str:
        """
        Определяет категорию возраста автомобиля (старая/новая).

        Считаем автомобиль старым, если его год выпуска меньше 2010.

        :return: 'старая' если год < 2010, иначе 'новая'

        >>> car = Car("Ford", 2005)
        >>> car.age_category()
        'старая'
        >>> car = Car("Tesla", 2018)
        >>> car.age_category()
        'новая'
        """
        return "старая" if self.year < 2010 else "новая"

    def country(self) -> str:
        """
        Возвращает страну производителя для известных моделей.

        В текущей реализации известна только модель "BMW" (Германия).
        Для остальных возвращается "Неизвестно".

        :return: название страны или "Неизвестно"

        >>> car = Car("BMW", 2019)
        >>> car.country()
        'Германия'
        >>> car = Car("Lada", 2010)
        >>> car.country()
        'Неизвестно'
        """
        countries = {"BMW": "Германия"}
        return countries.get(self.model, "Неизвестно")

# TODO работоспособность экземпляров класса проверить с помощью doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)


class Univer:
    """
    Класс, представляющий просмотр сериала "Универ".

    Атрибуты:
        look_series (int): количество просмотренных серий.
        full_series (int): общее количество серий в сезоне (от 1 до 100).
    """

    def __init__(self, look_series: int, full_series: int) -> None:
        """
        Инициализация объекта Univer.

        :param look_series: количество просмотренных серий (целое положительное число)
        :param full_series: общее количество серий (целое число от 1 до 100)
        :raises TypeError: если передан неверный тип данных
        :raises ValueError: если значение выходит за допустимые пределы
        """
        if not isinstance(look_series, int):
            raise TypeError("Количество просмотренных серий должно быть целым числом (int)")
        if look_series < 0:
            raise ValueError("Количество просмотренных серий не может быть отрицательным")
        self.look_series = look_series

        if not isinstance(full_series, int):
            raise TypeError("Общее количество серий должно быть целым числом (int)")
        if full_series <= 0 or full_series > 100:
            raise ValueError("Общее количество серий должно быть в диапазоне от 1 до 100")
        self.full_series = full_series

    def love_person(self) -> str:
        """
        Определяет любимого персонажа в зависимости от количества просмотренных серий.

        Правила:
            - от 0 до 24 серий — Гоша
            - от 25 до 49 серий — Кузя
            - от 50 до 99 серий — Майкл
            - при 100 и более сериях — неизвестно

        :return: имя персонажа (строка)
        """
        if 0 <= self.look_series < 25:
            return "Гоша"
        elif 25 <= self.look_series < 50:
            return "Кузя"
        elif 50 <= self.look_series < 100:
            return "Майкл"
        else:
            return "Неизвестно"

    def love_moment(self) -> str:
        """
        Возвращает любимый момент из сериала в зависимости от количества просмотренных серий.

        Правила:
            - от 0 до 24 серий — "Гоша уходит в армию из-за не сданной сессии"
            - от 25 до 49 серий — "Кузя поет песню шняга шняжная"
            - от 50 до 99 серий — "Майкл пытается заплакать"
            - при 100 и более сериях — "Момент неизвестен"

        :return: описание момента (строка)
        """
        if 0 <= self.look_series < 25:
            return "Гоша уходит в армию из-за не сданной сессии"
        elif 25 <= self.look_series < 50:
            return "Кузя поет песню шняга шняжная"
        elif 50 <= self.look_series < 100:
            return "Майкл пытается заплакать"
        else:
            return "Момент неизвестен"


if __name__ == "__main__":
    # Пример использования
    ser = Univer(45, 100)
    print("Количество серий в сезоне:", ser.full_series)
    print("Посмотрено серий:", ser.look_series)
    print("Любимый персонаж:", ser.love_person())
    print("Любимый момент:", ser.love_moment())
    # TODO работоспособность экземпляров класса проверить с помощью doctest


    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
