class Calculator:
    def __init__(self):
        """Processess the expresion to convert into numbers"""
        # {\frac{2}2} -> 2 + 2 + \derivative{2x};
        pass

    def sum(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def derivative(self, expression):
        pass

    def definite_integral(self, expression, a, b):
        pass

# Entidad: Propiedades y Métodos
from datetime import datetime
class User:
    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = datetime.fromisoformat(birthdate)

    def age(self):
        today = datetime.today()
        year_diff = today.year - self.birthdate.year
        rest_diff = ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        age = year_diff - rest_diff

        return age

    
    def fullname(self):
        return self.name + " " + self.surname
