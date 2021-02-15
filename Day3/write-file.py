
# with open("guest.txt", "w") as file:
#     file.write(name=input("Please enter your name: "))
#     file.write(name)


# name = input("Please enter your name: ")
# with open("guest.txt", "w") as file:
#     file.write(name)


# Ask user for input for their favorite dish. And write the name of the dish in the file.

# # You will read our favorite dishes file and display them on the screen


# favorite_dish = input("What is your favorite dish? ")
# with open("guest.txt", "w") as file:
#     content = file.write(favorite_dish)

# another_dish = input("What else do you like? ")
# with open("guest.txt", "a") as file:
#     other_content = file.write(another_dish)

with open("emails.txt") as file_object:
    email_list = file_object.read()

print(email_list)
duplicate_emails = email_list.split(',')
# Python 3 code to demonstrate
# removing duplicated from list
# using naive methods

# initializing list
# email_list
print("The original list is : " + str(duplicate_emails))

# # using naive method
# # to remove duplicated
# # from list
duplicate_free_emails = []
for email in duplicate_emails:
    email = email.strip()
    if email not in duplicate_free_emails:
        duplicate_free_emails.append(email)
# for i in email_list:
#     if i not in email_result:
#         email_result.append(i)

# # printing list after removal
# print("The list after removing duplicates : " + str(email_result))

with open("duplicate-free-email-list.txt", "w") as file_object:
    for email in duplicate_free_emails:
        file_object.write(email)
        file_object.write("\n")
