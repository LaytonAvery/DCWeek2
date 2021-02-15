from calculator_class import Calculator
import unittest


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.value = 0
        self.calculator = Calculator(value)

    def test_multiplication(self):
        calculator = Calculator()
        result = calculator.multiply(5)
        self.calculator.multiply(result)
        self.assertEqual(5, self.calculator.result)

    def test_addition(self):

    def tearDown(self):
        print("Test is done.")


unittest.main()


# def subtraction(first_number, second_number):
#     return first_number - second_number


# def multiplication(first_number, second_number):
#     return first_number*second_number


# def division(first_number, second_number):
#     return first_number/second_number


# def addition(first_number, second_number):
#     return first_number + second_number


# def calculator():
#     first_number = float(input("Enter your first number: "))

#     operand = input("Enter an operand: ")

#     second_number = float(input("Enter your second number: "))
#     if operand == "-":
#         subtraction(first_number, second_number)
#         answer = subtraction(first_number, second_number)

#     elif operand == "*":
#         multiplication(first_number, second_number)
#         answer = multiplication(first_number, second_number)

#     elif operand == "/":
#         division(first_number, second_number)
#         answer = division(first_number, second_number)

#     else:
#         addition(first_number, second_number)
#         answer = addition(first_number, second_number)

#     message = f"Your calculation is: {answer}"
#     print(message)


# calculator()
