#!/usr/bin/python3
import beverages
import random

class CoffeeMachine:
    def __init__(self):
        self.nb_services = 0

    class EmptyCup(beverages.HotBeverage):
        name = 'empty cup'
        price = '0.90'

        def Description(self):
            return 'An empty cup?! Gimme my money back!'

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__('This coffee machine has to be repaired.')

    def repair(self):
        self.nb_services = 0

    def serve(self, beverage: beverages.HotBeverage):
        if self.nb_services >= 10:
            raise self.BrokenMachineException
        self.nb_services += 1
        return random.choice([self.EmptyCup(), beverage])


if __name__ == '__main__':
    machine = CoffeeMachine()
    lst_items = list(beverages.__dict__.items())
    drinks = []
    for l in lst_items:
        drink_name = l[0]
        if not isinstance(l[1], type) or not issubclass(l[1], beverages.HotBeverage) or l[1] is beverages.HotBeverage:
            continue
        drinks.append(beverages.__dict__[drink_name]())
    for i in range(0,22):
        try:
            drink = machine.serve(random.choice(drinks))
            print(f'i = {i}, {drink}', end='\n\n')
        except Exception as e:
            print(e, end='\n\n')
            machine.repair()
