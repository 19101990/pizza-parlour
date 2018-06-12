class Customer:
    def __init__(self, name):
        self.name = name

    def order_food(self, server):
        print(self.name, 'orders from ', server.name)

    def pay(self, server):
        print(self.name, 'pays %s for the order' % server.name)
