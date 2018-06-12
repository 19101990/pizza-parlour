from employees import *
from equipment import *
from customer import *

class PizzaParlour:
    def __init__(self):
        self.server = Server("Matt")
        self.chef = Chef("Meg")
        self.owen = Owen()
        self.mixer = Mixer()

    def order(self, name):
        customer = Customer(name)
        self.server.take_order()
        customer.order_food(self.server)
        print('\n')
        self.mixer.make_dough()
        self.chef.cook()
        self.owen.bake()
        print('\n')
        self.server.serve()
        customer.pay(self.server)


action = PizzaParlour()
action.order("Evan")

