from person import Person
from pizza_menu import pizzas
from drink_menu import *

check = []

class Customer(Person):
    def __init__(self, name):
        super().__init__(name)

    def choose_pizza(self):
        global check
        pizza_choice = input('[HINT: type pizza name and hit enter]\n').upper()
        check.append(pizzas[pizza_choice])

    def choose_drink(self):
        global check
        drink_choice = input('[HINT: type drink name and hit enter]\n').upper()
        check.append(all_drinks[drink_choice])

    def eat_pizza(self):
        pass

    def get_check(self):
        pass

    def look_at_check(self):
        pass

    def pay_for_food(self):
        pass

