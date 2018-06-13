from employees import *
from equipment import *
from customer import *
import sys
import os
import time

class PizzaParlour:
    def __init__(self):
        self.server = Server("Matt")
        self.chef = Chef("Meg")
        self.owen = Owen()
        self.mixer = Mixer()

    def prompt_for_name(self):
        global name_option
        name_option = input('What\'s your name?\n')

    def order(self):
        self.prompt_for_name()
        customer = Customer(name_option)
        self.server.take_order()
        customer.order_food(self.server)
        time.sleep(4)
        os.system("cls")
        print('Your food is being prepared')
        
        self.mixer.make_dough()
        self.chef.cook()
        self.owen.bake()
        print('\n')
        self.server.serve()
        customer.pay(self.server)



action = PizzaParlour()
action.order()

