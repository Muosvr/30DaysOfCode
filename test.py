class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))

class Employee(Person):
    def __init__(self, name, age, staffNumber):
        super().__init__(name, age)
        self.staffNumber = staffNumber
    def display(self):
        super().display()
        print("Staff Number: " + str(self.staffNumber))

new_person = Person("Jason", 20)
new_person.display()

new_employee = Employee("Tom", 25, 2332)
new_employee.display()
