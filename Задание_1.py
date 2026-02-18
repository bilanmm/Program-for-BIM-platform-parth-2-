from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):  # TODO инициализировать объект "Стакан"
            raise ValueError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    glass1 = Glass(200, 100)
    glass2 = Glass(500, 50)

    incorreect_capacity_volume_type = -1
    incorrect_occupied_volume = 5


      # TODO инициализировать два объекта типа Glass

    # TODO попробовать инициализировать не корректные объекты
    print(glass1 is glass2)