from employees import *

class Customer:
    def __init__(self, name):
        self.name = name

    def order_food(self, server):
        print(self.name, 'orders from ', server.name)

    def pay(self, server):
        print(self.name, 'pays %s for the order' % server.name)



class PizzaParlour:
    def __init__(self):
        self.server = Server("Matt", "Baker", 3, 40000)
        self.chef = Chef("Meg", "O'Brien", 5, 60000)

    def order(self, name):
        customer = Customer(name)
        self.server.take_order()
        customer.order_food(self.server)
        self.chef.cook()
        self.server.serve()
        customer.pay(self.server)
        print('\n----------\n')


action = PizzaParlour()
action.order("Evan")
action.order("Caroline")
