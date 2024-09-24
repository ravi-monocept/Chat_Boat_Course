print("hello ravi")
price = 50
price_of_asset = 15
tax_percentage = 3

left_amount = price - (price_of_asset + price_of_asset * 0.03)
print(left_amount)

# days_until = input("Enter how many days your birthday until  :  ")

# week = 7
# week_left = round(int(days_until) / week, 2)
# print(f"total days {days_until} week left is {week_left}")


# Create a list of 5 animals called zoo

# - Delete the animal at the 3rd index.

# - Append a new animal at the end of the list

# - Delete the animal at the beginning of the list.

# - Print all the animals

# - Print only the first 3 animals

zoo = ["dog", "goat", "cow", "pig", "bufflow"]

zoo.pop(3)
print(zoo)

zoo.append("tiger")

zoo.pop(0)
print(zoo)

print(zoo[0:3])

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0
while i in range(3):
    i = i + 1
    for x in my_list:
        if x == "Monday":
            continue
        print(x, end=" ")
    print()


# - Create a function that takes in 3 parameters(firstname, lastname, age) and

# returns a dictionary based on those values


def person(firstname, lastname, age):
    details = {"firstname": firstname, "lastname": lastname, "age": age}
    
    return details
import json
print(json.dumps(person("Ravi","Kumar",27),indent=4))
