class Mixin:
    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Mixin):
    def __init__(self, name, price, quantity):
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}'
