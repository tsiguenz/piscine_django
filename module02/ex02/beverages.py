#!/usr/bin/python3

class HotBeverage:
    name = 'hot beverage'
    price = '0.30'

    def Description(self) -> str:
        return 'Just some hot water in a cup.'

    def __str__(self):
        str = f'name : {self.name}\n'
        str += f'price : {self.price}\n'
        str += f'description : {self.Description()}'
        return str


class Coffee(HotBeverage):
    name = 'coffee'
    price = '0.40'

    def Description(self) -> str:
        return 'A coffee, to stay awake.'


class Tea(HotBeverage):
    name = 'tea'


class Chocolate(HotBeverage):
    name = 'chocolate'
    price = '0.50'

    def Description(self) -> str:
        return 'Chocolate, sweet chocolate...'


class Cappuccino(HotBeverage):
    name = 'cappuccino'
    price = '0.45'

    def Description(self) -> str:
        return "Un po' di Italia nella sua tazza!"


if __name__ == '__main__':
    print(HotBeverage(), end='\n\n')
    print(Coffee(), end='\n\n')
    print(Tea(), end='\n\n')
    print(Chocolate(), end='\n\n')
    print(Cappuccino())
