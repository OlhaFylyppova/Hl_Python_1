# Створіть клас «Правильний дріб» та реалізуйте методи порівняння, додавання, віднімання та множення
# для екземплярів цього класу.

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        print(f"Result mul: {self.a * other.a}/{self.b * other.b}")
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        print(f"Result add: {self.a * other.b + self.b * other.a}/{self.b * other.b}")
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def __sub__(self, other):
        print(f"Result sub: {self.a * other.b - self.b * other.a}/{self.b * other.b}")
        return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)

    def __eq__(self, other):
        if self.a * other.b == self.b * other.a:
            print(f"Result eq: {self.a}/{self.b} is equal {other.a}/{other.b}")
        else:
            print(f"Result eq: {self.a}/{self.b} is not equal {other.a}/{other.b}")
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        if self.a * other.b > self.b * other.a:
            print(f"Result gt: {self.a}/{self.b} is greater than {other.a}/{other.b}")
        else:
            print(f"Result gt: {self.a}/{self.b} is less than {other.a}/{other.b}")
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        if self.a * other.b < self.b * other.a:
            print(f"Result lt: {self.a}/{self.b} is less than {other.a}/{other.b}")
        else:
            print(f"Result lt: {self.a}/{self.b} is greater than {other.a}/{other.b}")
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
