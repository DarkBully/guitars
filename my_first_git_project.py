class Person:
    def __init__(self, name, age, job, salary):
        self.name = name
        self.age = age
        self.job = job
        self.__salary = salary
    
    def work(self):
        return f'{self.name} working in {self.job} for {self.__salary}'

class Policman(Person):
    pass

pol = Policman('Adam', 45, input('Enter a job name: '), 3000)
print(pol.work())