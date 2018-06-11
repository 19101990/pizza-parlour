class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Employee(Person):
    def __init__(self, name, surname, years_in_company, salary = 0):
        super().__init__(name, surname)
        self.salary = salary
        self.name = name
        self.surname = surname
        self.years_in_company = years_in_company


class Chef(Employee):
    def __init__(self, name, surname, years_in_company, salary):
        super().__init__(name, surname, years_in_company, salary)

    def cook(self):
        print(self.name, 'is cooking')


class Server(Employee):
    def __init__(self, name, surname, years_in_company, salary):
        super().__init__(name, surname, years_in_company, salary)

    def take_order(self):
        print('Hi!, my name is ', self.name, '. What can I get you?')

    def serve(self):
        print(self.name, 'is serving the meal')



