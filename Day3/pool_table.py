import time

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%m/%d/%y at %I:%M %p")
pool_tables = []


class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.start_time = None
        self.end_time = None
        self.total_time_played = now

    def check_out(self):
        self.is_occupied = True
        self.start_time = datetime.now()

    def check_in(self):
        self.is_occupied = False
        self.end_time = datetime.now()
        print(f"Table Number: {pool_table.table_number} ----Start Time: {pool_table.start_time} ----End Time: {pool_table.end_time} ----Total Time Played: {pool_table.total_time_played}")

    def total_time_played(self):
        total_time_played = self.end_time - self.start_time


for index in range(1, 13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)


def display_menu():
    print("***************************************")
    print("""
        Welcome to the pool hall!
        1. Display Tables
        2. Check out a Table
        3. Check in a Table
        4. Press q to quit
    """)
    print("***************************************")
    print("\n")


def display_tables():
    for index in range(0, len(pool_tables)):
        pool_table = pool_tables[index]
        if pool_table.is_occupied == False:
            availability = "is available"
            print(f"Table Number: {pool_table.table_number} {availability}")
        elif pool_table.is_occupied == True:
            availability = "is not available"
            formatted_start_time = pool_table.start_time.strftime(
                "%m/%d/%y at %I:%M %p")
            print(
                f"Table Number: {pool_table.table_number} {availability} ----Start Time: {pool_table.start_time}")


while True:
    display_menu()
    choice = input("What would you like to do? ")
    if choice == "1":
        display_tables()

    elif choice == "2":
        display_tables()

        table_checkout_index = int(
            input(f"\nWhat table would you like to checkout? "))
        table = pool_tables[table_checkout_index - 1]
        table.check_out()

    elif choice == "3":
        display_tables()

        table_checkin_index = int(
            input("Which table would you like to check in? "))
        table = pool_tables[table_checkin_index - 1]
        table.check_in()

    elif choice == "q":
        break
    else:
        print("Try again.")
