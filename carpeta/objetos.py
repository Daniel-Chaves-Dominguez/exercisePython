class Persona:
    def __init__(self, name=None, age=0, weight=0, height=0, race=None, nationality=None):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.race = race
        self.nationality = nationality

    def greetings(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")

    def add_years(self,years):
        self.age += years

    def __str__(self):
        return f'{self.name} who is {self.nationality}'


class Teacher(Persona):
    def __init__(self, name=None, age=0, weight=0, height=0, race=None, nationality=None, salary=1200, subject='Programming'):
        super().__init__(name, age, weight, height, race, nationality)
        self.salary = salary
        self.subject = subject

    def __str__(self):
        return f'{self.name}, teacher of {self.subject}'

teacher = Teacher('Brandon', 21, 65, 1.7, 'Homo sapiens', 'Bolivian', 3000, 'AI Agents')
print(teacher)

