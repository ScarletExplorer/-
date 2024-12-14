import doctest

class Cup:
    def __init__(self, material: str, volume: float, color: str):
        """
        Создание и подготовка к работе объекта "Чашка"

        :param material: Материал чашки
        :param volume: Объем чашки в миллилитрах
        :param color: Цвет чашки

        Примеры:
        >>> cup = Cup("ceramic", 300, "blue")
        """
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("Объем чашки должен быть положительным числом.")
        self.material = material
        self.volume = volume
        self.color = color

    def fill(self, liquid: str, amount: float) -> None:
        """
        Метод для наполнения чашки.

        :param liquid: Тип жидкости
        :param amount: Объем жидкости в миллилитрах

        :raises ValueError: Если объем жидкости превышает вместимость чашки

        Примеры:
        >>> cup = Cup("ceramic", 300, "blue")
        >>> cup.fill("water", 200)
        """
        if amount > self.volume:
            raise ValueError("Объем жидкости превышает вместимость чашки.")
        ...

    def drink(self, amount: float) -> None:
        """
        Метод для питья из чашки.

        :param amount: Объем жидкости, который выпивают

        :raises ValueError: Если объем выпиваемой жидкости больше текущего

        Примеры:
        >>> cup = Cup("ceramic", 300, "blue")
        >>> cup.drink(50)
        """
        if amount < 0:
            raise ValueError("Объем выпиваемой жидкости не может быть отрицательным.")
        ...

    def clean(self) -> None:
        """
        Метод для очистки чашки.

        Примеры:
        >>> cup = Cup("ceramic", 300, "blue")
        >>> cup.clean()
        """
        ...

class Phone:
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param brand: Бренд телефона
        :param model: Модель телефона
        :param battery_capacity: Емкость аккумулятора в мАч

        Примеры:
        >>> phone = Phone("Samsung", "Galaxy S21", 4000)
        """
        if battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным числом.")
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

    def make_call(self, number: str) -> None:
        """
        Метод для осуществления звонка.

        :param number: Номер телефона, на который совершается звонок

        Примеры:
        >>> phone = Phone("Samsung", "Galaxy S21", 4000)
        >>> phone.make_call("+123456789")
        """
        ...

    def send_message(self, number: str, message: str) -> None:
        """
        Метод для отправки сообщения.

        :param number: Номер телефона получателя
        :param message: Текст сообщения

        Примеры:
        >>> phone = Phone("Samsung", "Galaxy S21", 4000)
        >>> phone.send_message("+123456789", "Hello!")
        """
        ...

    def charge(self, amount: int) -> None:
        """
        Метод для зарядки телефона.

        :param amount: Количество заряда, добавляемое в аккумулятор (мАч)

        :raises ValueError: Если количество заряда отрицательное

        Примеры:
        >>> phone = Phone("Samsung", "Galaxy S21", 4000)
        >>> phone.charge(500)
        """
        if amount < 0:
            raise ValueError("Количество заряда должно быть положительным числом.")
        ...

class Street:
    def __init__(self, name: str, length: float, num_buildings: int):
        """
        Создание и подготовка к работе объекта "Улица"

        :param name: Название улицы
        :param length: Длина улицы в километрах
        :param num_buildings: Количество зданий на улице

        Примеры:
        >>> street = Street("Main Street", 2.5, 10)
        """
        if length <= 0:
            raise ValueError("Длина улицы должна быть положительным числом.")
        if num_buildings < 0:
            raise ValueError("Количество зданий не может быть отрицательным.")
        self.name = name
        self.length = length
        self.num_buildings = num_buildings

    def repair(self) -> None:
        """
        Метод для ремонта улицы.

        Примеры:
        >>> street = Street("Main Street", 2.5, 10)
        >>> street.repair()
        """
        ...

    def clean(self) -> None:
        """
        Метод для уборки улицы.

        Примеры:
        >>> street = Street("Main Street", 2.5, 10)
        >>> street.clean()
        """
        ...

    def add_building(self) -> None:
        """
        Метод для добавления здания на улице.

        Примеры:
        >>> street = Street("Main Street", 2.5, 10)
        >>> street.add_building()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации