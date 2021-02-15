# Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.


with open("guest.txt", "w") as file:
    file.write(name=input("Please enter your name: "))
    file.write(name)
