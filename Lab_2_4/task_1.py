class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int):
        """
        Конструктор класса Animal.

        :param name: Имя животного
        :param age: Возраст животного
        """
        self._name = name  # Инкапсуляция имени (предположим, что имя нельзя менять напрямую)
        self.age = age

    def make_sound(self) -> str:
        """
        Метод, который должны переопределять дочерние классы.
        """
        return "Какой-то звук"

    def __str__(self) -> str:
        """
        Человекочитаемое представление объекта.
        """
        return f"Животное: {self._name}, возраст: {self.age}"

    def __repr__(self) -> str:
        """
        Официальное строковое представление объекта.
        """
        return f"Animal(name={self._name}, age={self.age})"


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.

        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        """
        Переопределённый метод из базового класса.
        Собака лает, поэтому переопределяем звук.
        """
        return "Гав-гав!"

    def __str__(self) -> str:
        """
        Переопределение метода для более специфичного вывода.
        """
        return f"Собака: {self._name}, порода: {self.breed}, возраст: {self.age}"


class Cat(Animal):
    """
    Дочерний класс, представляющий кошку.
    """

    def __init__(self, name: str, age: int, color: str):
        """
        Конструктор класса Cat.

        :param name: Имя кошки
        :param age: Возраст кошки
        :param color: Окрас кошки
        """
        super().__init__(name, age)
        self.color = color

    def make_sound(self) -> str:
        """
        Переопределение метода make_sound().
        Кошки не лают, а мяукают.
        """
        return "Мяу-мяу!"

    def __str__(self) -> str:
        """
        Переопределение метода для более специфичного вывода.
        """
        return f"Кошка: {self._name}, окрас: {self.color}, возраст: {self.age}"