import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self) -> any:
        return self.__name

    @name.setter
    def name(self, name):
        """Метод срабатывает при операции присваивания."""
        if len(name) < 11:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине. Без учета скидки.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price * self.pay_rate)

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Item.all.append(Item(row['name'], row['price'], row['quantity']))

    @staticmethod
    def string_to_number(string):
        return int(float(string))
