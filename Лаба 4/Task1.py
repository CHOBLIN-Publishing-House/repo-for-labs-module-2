import doctest
from datetime import datetime

class House:
    """ Базовый класс дома"""
    def __init__(self, address: str, number_of_floors: int) -> None:
        self._address = address # инициализируем защищенный атрибут, так как адрес у дома не так-то просто изменить
        self._number_of_floors = number_of_floors # инициализируем защищенный атрибут, чтобы случайно не изменить этажность дома

    @property   # метод геттер для address
    def address(self) -> str:
        """Возвращает адрес дома"""
        return self._address

    @address.setter # метод сеттер для address
    def address(self, new_address: str) -> None:
        """Устанавливает адрес дома"""
        self._address = str(new_address) # адрес можно не проверять, а приводить к строковому представлению

    @property  # метод геттер для number_of_floors
    def number_of_floors(self) -> int:
        """Возвращает этажность дома"""
        return self._number_of_floors

    @number_of_floors.setter  # метод сеттер для number_of_floors
    def number_of_floors(self, new_number_of_floors: int) -> None:
        """Устанавливает этажность дома"""
        if not isinstance(new_number_of_floors, int):
            raise TypeError("Этажность дома должна быть типа int")
        if new_number_of_floors <= 0:
            raise ValueError("Этажность дома должна быть положительным числом")
        self._number_of_floors = new_number_of_floors

    def __str__(self) -> str:
        return f"Дом по адресу {self.address} высотой {self.number_of_floors} этажей"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(address={self.address!r}, number_of_floors={self.number_of_floors})"

    @classmethod
    def can_we_do_party(cls) -> bool:
        """Метод, который показывает, можем ли мы провести вечеринку в доме"""
        return True # дом же наш, так что можно

class DetachedHouse(House):
    """Дочерний класс особняка"""
    def __init__(self, address: str, number_of_floors: int, square: int) -> None:
        super().__init__(address, number_of_floors)
        self._square = square # инициализируем защищенный атрибут, потому что площадь дома не меняется

    #Методы геттеры и сеттеры для address и number_of_floors наследуются

    @property   # метод геттер для square
    def square(self) -> int:
        """Возвращает площадь особняка"""
        return self._square

    @square.setter   # метод сеттер для square
    def square(self, new_square: int) -> None:
        """Устанавливает площадь особняка"""
        if not isinstance(new_square, int):
            raise TypeError("Площадь должна быть типа int")
        if new_square <= 0:
            raise ValueError("Площадь должна быть больше нуля")
        self._square = new_square

    # Метод str наследуется от родительского класса

    # Метод repr перегружается для соответствия дочернему классу
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(address={self.address!r}, number_of_floors={self.number_of_floors}, square={self.square})"

    # Метод can_we_do_party наследуется

class TenementHouse(House):
    """Дочерний класс многоквартирного дома"""
    def __init__(self, address: str, number_of_floors: int, number_of_flats: int) -> None:
        super().__init__(address, number_of_floors)
        self._number_of_flats = number_of_flats # инициализируем защищенный атрибут, ведь комнату потерять трудно

    # Методы геттеры и сеттеры для address и number_of_floors наследуются

    @property   # метод геттер для number_of_flats
    def number_of_flats(self) -> int:
        """Возвращает количество квартир многоквартирного дома"""
        return self._number_of_flats

    @number_of_flats.setter   # метод сеттер для number_of_flats
    def number_of_flats(self, new_number_of_flats: int) -> None:
        """Устанавливает количество квартир многоквартирного дома"""
        if not isinstance(new_number_of_flats, int):
            raise TypeError("Количество квартир должно быть типа int")
        if new_number_of_flats <= 0:
            raise ValueError("Количество квартир должно быть больше нуля")
        self._number_of_flats = new_number_of_flats

    # Метод str наследуется от родительского класса

    # Метод repr перегружается для соответствия дочернему классу
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(address={self.address!r}, number_of_floors={self.number_of_floors}, number_of_flats={self.number_of_flats})"

    # Метод can_we_do_party перегружается из-за особенностей многоквартирных домов
    @classmethod
    def can_we_do_party(cls) -> bool:
        """Метод, который показывает, можем ли мы провести вечеринку в квартире"""
        """В квартире нельзя шуметь с 22:00 до 8:00"""
        current_datetime = datetime.now() # получаем текущее время
        if current_datetime.hour < 8 or current_datetime.hour >= 22:
            return False # если слишком рано или слишком поздно, вечеринка отменяется
        else:
            return True



if __name__ == "__main__":
    print('Проверка лабораторной')
    print()

    time_right_now = current_datetime = datetime.now()
    print("Сейчас ровно",  time_right_now.hour, "часов", time_right_now.minute, "минут")
    print()

    house1 = House('Политехническая ул., 29', 3)
    print(house1)
    print("Выражен строкой", str(house1))
    print("Может быть определен как", repr(house1)) # House(address='Политехническая ул., 29', number_of_floors=3)
    print("По адресу", house1.address)
    print("Имеет этажей", house1.number_of_floors)
    print("Может потусить?", house1.can_we_do_party())
    print()

    house2 = DetachedHouse('Новороссийская ул., 50', 4, 666)
    print(house2)
    print("Выражен строкой", str(house2))
    print("Может быть определен как", repr(house2)) # DetachedHouse(address='Новороссийская ул., 50', number_of_floors=5, square=666)
    print("По адресу", house2.address)
    print("Имеет этажей", house2.number_of_floors)
    print("Площадью", house2.square)
    print("Может потусить?", house2.can_we_do_party())
    print()

    house3 = TenementHouse('Парголовская ул., 11, к. 2', 5, 5 * 15)
    print(house3)
    print("Выражен строкой", str(house3))
    print("Может быть определен как", repr(house3))  # TenementHouse(address='Парголовская ул., 11, к. 2', number_of_floors=5, number_of_flats=75)
    print("По адресу", house3.address)
    print("Имеет этажей", house3.number_of_floors)
    print("У него квартир", house3.number_of_flats)
    print("Может потусить?", house3.can_we_do_party())
    print()

    print('Всё работает')
    print('Ура!')
