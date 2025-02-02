class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name   # инициализируем защищенный атрибут
        self._author = author    # инициализируем защищенный атрибут

    @property   # метод геттер для name
    def name(self) -> str:
        """Возвращает название книги"""
        return self._name

    @property   # метод геттер для author
    def author(self) -> str:
        """Возвращает автора книги"""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    """Дочерний класс бумажной книги"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages


    @property   # метод геттер для pages
    def pages(self) -> int:
        """Возвращает количество страниц в книге"""
        return self._pages

    @pages.setter   # метод сеттер для pages
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц в книге"""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = pages

    """Метод str наследуется от родительского класса"""

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook:
    """Дочерний класс аудиокниги"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property  # метод геттер для duration
    def duration(self) -> float:
        """Возвращает продолжительность книги"""
        return self._duration

    @duration.setter  # метод сеттер для duration
    def duration(self, duration: float) -> None:
        """Устанавливает продолжительность книги"""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность книги должна быть больше нуля")
        self._duration = duration

    """Метод str наследуется от родительского класса"""

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
