from person import Person
from pizza_menu import pizzas

check = []

class Customer(Person):
    def __init__(self, name):
        super().__init__(name)

    def choose_pizza(self):
        global check
        choice = input('[HINT: type pizza name and hit enter]\n')
        choice = choice.upper()
        check.append(pizzas[choice])
        print(check)

    def eat_pizza(self):
        pass

    def get_check(self):
        pass

    def look_at_check(self):
        pass

    def pay_for_food(self):
        pass

