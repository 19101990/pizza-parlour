from person import Person
from customer import Customer
from pizza_menu import pizzas
from drink_menu import *
import sys
import os
import time


class Employee(Person):
    def __init__(self, name, salary = 0):
        super().__init__(name)
        self.salary = salary


class Server(Employee):
    def __init__(self, name, salary = 0):
        super().__init__(name, salary)

    def introduce(self):
        print('Hi! My name is {}. What\'s your name?'.format(self.name))
        global name_option
        name_option = input('')
        global c
        c = Customer(name_option)
        print('Nice to meet you, {}!'.format(c.name))
        time.sleep(1)
        print('Here\'s our menu:')
        time.sleep(2)

    def show_pizza_menu(self):
        os.system("cls")
        for i in pizzas:
            print(i, pizzas[i])

    def ask_if_something_else(self):
        choice = input('Would you like to order something else?\n')
        if choice == 'y' or choice == 'yes':
            self.show_pizza_menu()
        elif choice == 'n' or choice == 'no':
            self.offer_drinks()
        else:
            self.ask_if_something_else()

    def offer_drinks(self):
        choice = input('Would you like something to drink with your pizza?\n')
        if choice == 'y' or choice == 'yes':
            self.show_drink_menu()
        elif choice == 'n' or choice == 'no':
            print('Very well. I will bring your meal shortly.')
        else:
            self.offer_drinks()

    def show_drink_menu(self):
        os.system('cls')
        print('SOFT DRINKS')
        for i in drinks:
            print(i, drinks[i])
        print('\nBEERS')
        for i in beers:
            print(i, beers[i])
        print('\nWINE')
        for i in wine:
            print(i, wine[i])

    def serve_drinks(self):
        pass

    def serve_pizza(self):
        pass

    def bring_check(self):
        pass


class Cook(Employee):
    def __init__(self, name, salary = 0):
        super().__init__(name, salary)

    def make_pizza(self):
        pass

s = Server("Matt")
s.introduce()
s.show_pizza_menu()
c.choose_pizza()
s.ask_if_something_else()
c.choose_pizza()
s.offer_drinks()
