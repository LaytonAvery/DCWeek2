# Take a look at the following code:

# number = int(input("Enter number: "))
# What would happen if you input a character instead of a number?

# What type of exception will be thrown?

# Can you write code to capture the exception so the program does not abort?


# number = int("Enter a number: ")


try:

    number = int(input("Enter a number: "))

except ZeroDivisionError:
    print("Can't divide by zero.")

except TypeError:
    print("Please do not enter decimal numbers.")

except ValueError:
    print("Please enter numbers only.")

else:
    print("Done.")
