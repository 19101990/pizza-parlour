class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary = 0):
        super().__init__(name)
        self.salary = salary


class Chef(Employee):
    def __init__(self, name, salary = 0):
        super().__init__(name, salary)

    def cook(self):
        print('>', self.name, 'is making the sauce')
        print('>', self.name, 'is making the pizza')


class Server(Employee):
    def __init__(self, name, salary = 0):
        super().__init__(name, salary)

    def take_order(self):
        print(self.name, ': Hi!, my name is ', self.name,
              '. What can I get you?')

    def serve(self):
        print(self.name, ': Here\'s your order.')



