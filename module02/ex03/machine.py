#!/usr/bin/python3
import beverages
import random


class CoffeeMachine:
    def __init__(self):
        self.nb_services = 0

    class EmptyCup(beverages.HotBeverage):
        name = "empty cup"
        price = "0.90"

        def Description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.nb_services = 0

    def serve(self, beverage: beverages.HotBeverage):
        if self.nb_services >= 10:
            raise self.BrokenMachineException
        self.nb_services += 1
        return random.choice([self.EmptyCup(), beverage])


def is_child_of(to_check, base_type):
    return (
        isinstance(to_check, type)
        and issubclass(to_check, base_type)
        and to_check is not base_type
    )


def get_list_of_available_beverages(lst_items):
    available_beverages = []
    for item in lst_items:
        drink_name = item[0]
        if not is_child_of(item[1], beverages.HotBeverage):
            continue
        available_beverages.append(beverages.__dict__[drink_name]())
    return available_beverages


if __name__ == "__main__":
    machine = CoffeeMachine()
    lst_items = list(beverages.__dict__.items())
    available_beverages = get_list_of_available_beverages(lst_items)
    for i in range(0, 22):
        try:
            beverage = machine.serve(random.choice(available_beverages))
            print(f"i = {i}, {beverage}", end="\n\n")

        except Exception as e:
            print(e, end="\n\n")
            machine.repair()
