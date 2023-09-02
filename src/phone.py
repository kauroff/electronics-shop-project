from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})'

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        """
        Метод срабатывает, когда используется оператор сложения.
        В параметре other хранится то, что справа от знака +
        """
        return self.quantity + other.quantity

    # @property
    # def number_of_sim(self) -> int:
    #     return self.number_of_sim
    #
    # @number_of_sim.setter
    # def number_of_sim(self, number_of_sim):
    #     """Метод срабатывает при операции присваивания."""
    #     if number_of_sim > 0:
    #         self.number_of_sim = number_of_sim
    #     else:
    #         return 'ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.'
