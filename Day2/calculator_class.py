class Calculator:
    def __init__(self, value):
        self.value = 0

    def multiply(self, number):
        self.value *= number

    def add(self, number):
        self.value += number

    def subtract(self, number):
        self.value -= number

    def divide(self, number):
        self.value /= number
