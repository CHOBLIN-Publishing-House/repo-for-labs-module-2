import doctest

class House:
    def __init__(self, number_of_flats: int, number_of_residents: int):
        """
        Создание и подготовка к работе объекта "Дом"

        :param number_of_flats: Количество квартир
        :param number_of_residents: Количество жильцов

        Примеры:
        >>> house = House(100, 500)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_flats, int):
            raise TypeError("Количество квартир должно быть типа int")
        if number_of_flats <= 0:
            raise ValueError("Количество квартир должно быть положительным числом")
        self.number_of_flats = number_of_flats

        if not isinstance(number_of_residents, int):
            raise TypeError("Количество жильцов должно быть типа int")
        if number_of_residents < 0:
            raise ValueError("Количество жильцов не может быть отрицательным числом")
        self.number_of_residents = number_of_residents

    def is_empty_house(self) -> bool:
        """
        Функция которая проверяет является ли дом пустым

        :return: Является ли дом пустым

        Примеры:
        >>> house = House(500, 0)
        >>> house.is_empty_house()
        """
        ...

    def add_residents_to_house(self, residents: int) -> None:
        """
        Заселение новых жильцов в дом.
        :param residents: Количество новых жильцов

        Примеры:
        >>> house = House(500, 0)
        >>> house.add_residents_to_house(200)
        """
        if not isinstance(residents, int):
            raise TypeError("Количество жильцов должно быть типа int")
        if residents < 0:
            raise ValueError("Количество новых жильцов должно быть положительным числом")
        ...

    def remove_residents_from_house(self, number_of_moved: int) -> None:
        """
        Выселение жильцов из дома.

        :param number_of_moved: Количество переехавших жильцов
        :raise ValueError: Если количество переехавших жильцов превышает количество нынешних жильцов,
        то возвращается ошибка.

        Примеры:
        >>> house = House(500, 500)
        >>> house.remove_residents_from_house(200)
        """
        if not isinstance(number_of_moved, int):
            raise TypeError("Количество жильцов должно быть типа int")
        if number_of_moved < 0:
            raise ValueError("Количество переехавших жильцов должно быть положительным числом")

        ...


class Youtube_channel:
    def __init__(self, number_of_subscribers: int, number_of_videos: int):
        """
        Создание и подготовка к работе объекта "Ютуб-канал"

        :param number_of_subscribers: Количество подписчиков
        :param number_of_videos: Количество роликов

        Примеры:
        >>> youtube_channel = Youtube_channel(100000, 50)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_subscribers, int):
            raise TypeError("Количество подписчиков должно быть типа int")
        if number_of_subscribers < 0:
            raise ValueError("Количество подписчиков не может быть отрицательным числом")
        self.number_of_subscribers = number_of_subscribers

        if not isinstance(number_of_videos, int):
            raise TypeError("Количество роликов должно быть типа int")
        if number_of_videos < 0:
            raise ValueError("Количество роликов не может быть отрицательным числом")
        self.number_of_videos = number_of_videos

    def add_subscribers_to_channel(self, subscribers: int) -> None:
        """
        Появление новых подписчиков на канале.
        :param subscribers: Количество новых подписчиков

        Примеры:
        >>> youtube_channel = Youtube_channel(500, 0)
        >>> youtube_channel.add_subscribers_to_channel(200)
        """
        if not isinstance(subscribers, int):
            raise TypeError("Количество подписчиков должно быть типа int")
        if subscribers < 0:
            raise ValueError("Количество новых подписчиков должно быть положительным числом")
        ...

    def release_new_video(self) -> None:
        """
        Функция, которая увеличивает количество видео-роликов на канале на единицу

        Примеры:
        >>> youtube_channel = Youtube_channel(500, 0)
        >>> youtube_channel.release_new_video()
        """
        ...


class Boyfriend:
    def __init__(self, handsome: bool, clever: bool, rich: bool):
        """
        Создание и подготовка к работе объекта "Парень"

        :param handsome: Красив ли.
        :param clever: Умен ли.
        :param rich: Богат ли.

        Примеры:
        >>> boyfriend = Boyfriend(True, True, False)  # инициализация экземпляра класса
        """

        if (not handsome) and rich:
            raise ValueError("Богат, но не красив? Невиданно!")
        self.handsome = handsome
        self.clever = clever
        self.rich = rich

    def is_rich_boyfriend(self) -> bool:
        """
        Функция которая проверяет является ли парень богатым

        :return: Является ли парень богатым

        Примеры:
        >>> boyfriend = Boyfriend(True, True, False)
        >>> boyfriend.is_rich_boyfriend()
        """
        ...

    def falling_in_love(self) -> None:
        """
        Влюбление. Делает парня красивым независимо от начальных данных.

        Примеры:
        >>> boyfriend = Boyfriend(False, False, False)
        >>> boyfriend.falling_in_love()
        """
        ...

    def is_ideal_boyfriend(self) -> bool:
        """
        Функция которая проверяет идеальность парня

        :return: Является ли парень идеальным

        Примеры:
        >>> boyfriend = Boyfriend(True, True, True)
        >>> boyfriend.is_ideal_boyfriend()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

