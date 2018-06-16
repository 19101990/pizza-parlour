from person import Person
from customer import Customer
from pizza_menu import pizzas
import time


# ------- Employee ------- #

class Employee(Person):
    def __init__(self, name, salary = 0):
        super().__init__(name)
        self.salary = salary


# ------- SERVER ------- #

class Server(Employee):
    def __init__(self, name, salary = 0):
        super().__init__(name, salary)

    def introduce(self):
        print('Hi! My name is {}. What\'s your name?'.format(self.name))
        global name_option
        name_option = input('')
        c = Customer(name_option)
        print('Nice to meet you, {}!'.format(c.name))
        time.sleep(1)
        print('Here\'s our menu:')
        time.sleep(2)

    def show_pizza_menu(self):
        print('\n')
        for i in pizzas:
            print(i, pizzas[i])

    def offer_drinks(self):
        pass

    def serve_drinks(self):
        pass

    def serve_pizza(self):
        pass

    def bring_check(self):
        pass


# ------- COOK ------- #

class Cook(Employee):
    def __init__(self, name, salary = 0):
        super().__init__(name, salary)

    def make_pizza(self):
        pass

s = Server("Matt")
s.introduce()
s.show_pizza_menu()

