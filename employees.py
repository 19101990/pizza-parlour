from person import Person
from customer import Customer
from equipment import Owen
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

    pizza_served = 0
    
    def __init__(self, name, salary = 0):
        super().__init__(name, salary)

    def introduce(self):
        os.system('cls')
        print('Hi! My name is {}. What\'s your name?'.format(self.name))
        global name_option
        name_option = input('')
        global c
        c = Customer(name_option)
        print('Nice to meet you, {}!'.format(c.name))
        time.sleep(1)
        print('Here\'s our menu:')
        time.sleep(2)
        self.show_pizza_menu()

    def show_pizza_menu(self):
        os.system("cls")
        for i in pizzas:
            print(i, pizzas[i])
        c.choose_pizza()
        self.ask_if_something_else()

    def ask_if_something_else(self):
        yNchoice = input('Would you like to order something else?\n')
        if yNchoice == 'y' or yNchoice == 'yes':
            self.show_pizza_menu()
        elif yNchoice == 'n' or yNchoice == 'no':
            self.offer_drinks()
        else:
            self.ask_if_something_else()

    def offer_drinks(self):
        yNchoice = input('Would you like something to drink with your pizza?\n')
        if yNchoice == 'y' or yNchoice == 'yes':
            self.show_drink_menu()
        elif yNchoice == 'n' or yNchoice == 'no':
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
        c.choose_drink()
        self.ask_if_something_else_to_drink()

    def ask_if_something_else_to_drink(self):
        yNchoice = input('Would you like to order something else to drink?\n')
        if yNchoice == 'y' or yNchoice == 'yes':
            self.show_drink_menu()
        elif yNchoice =='n' or yNchoice == 'no':
            if self.pizza_served:
                print('Very well. Enjoy your meal!')
                # CUSTOMER EATING PIZZA
                c.eat_pizza()
            elif not self.pizza_served:
                chef = Chef('Megan')
                chef.process_order()
        else:
            self.ask_if_smething_else_to_drink()


    def serve_pizza(self):
        self.pizza_served = 1
        os.system('cls')
        print('Here\'s your pizza, {}. '.format(c.name), end='')
        self.ask_if_something_else_to_drink()

    def bring_check(self):
        pass



class Chef(Employee):
    def __init__(self, name, salary = 0):
        super().__init__(name, salary)

    def process_order(self):
        os.system('cls')
        print('Your order is being processed')
        time.sleep(1)
        os.system('cls')
        print('Your order is being processed.')
        time.sleep(1)
        os.system('cls')
        print('Your order is being processed..')
        time.sleep(1)
        os.system('cls')
        print('Your order is being processed...')
        time.sleep(1)
        os.system('cls')
        print('Your order is being processed')
        time.sleep(1)
        os.system('cls')
        print('Your order is being processed.')
        time.sleep(1)
        os.system('cls')
        print('Your order is being processed..')
        time.sleep(1)
        os.system('cls')
        print('Your order is being processed...')
        time.sleep(1)
        s.serve_pizza()



        
        
s = Server("Matt")
s.introduce()
