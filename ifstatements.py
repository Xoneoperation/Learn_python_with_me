#Now we will be talking sbout if statements in python
#An if statement is used to check a condition and execute a block of code if the condition is true.
#We can use if statements to make decisions in our code.
cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
for car in cars:
    if car == "Honda":
        print(car.upper())
    else:
        print(car.title())
#We can also use if statements to check multiple conditions.
age = 20
age < 21
# requested_topping = ["mushrooms", "extra cheese"]
# 'mushrooms' in requested_topping

# banned_users = ["alice", "bob", "charlie"]
# user = "david"
# if user not in banned_users:
#     print(f"{user.lower()} is allowed to post a reponse.")
    #We can also use if statements to check if a value is in a list.

#we will create a boolean expersion to chek if a value is true or false 
rate = 1550
print(rate ==  2000) # This will print True if rate is less than 2000, otherwise False

food = "rice"
print(food == "rice" )
#This will print True if food is equal to "rice", otherwise False

friend = ['maxwell', 'adeola', 'timilehin', 'titilayo']
if 'titilayo' in friend:
    print("Titilayon is a friend of mine")
else:
    print("Titilayo is not a friend of mine")

banks = ['access', 'gtb', 'zenith', 'first bank']
if 'access' not in banks:
    print("Access bank is not in the lists of bannks")
else:
    print("Access banks is one of my favorite banks in this list of bansks")
age = 20
if age <= 10:
    print("You're not eligible to register")
else:
    print("You're eligible to register") 
#We can also use if statements to check if a value is greater than or less than another value.

requested_toppings = ["mushrooms", "extra cheese", "pepperoni", "green peppers"]
for requested_topping in requested_toppings:
    if requested_topping == "extra cheese" :
        print("sorry, we're ouut of  extra cheese")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

requested_topp = []
if requested_topp:
    for requested_topping in requested_topp:
        print(f"Adding {requested_topping}")
else:
    print("Are you sure you want a plain pizza?")

#Using multiple list 

available_toppings = ["mushrooms", "pepperoni", "green peppers", "extra cheese", "pineapple", "spinach", "kethup",
                       "chicken", "beef", "sausage"]
requested_toppings = ["mushrooms", "extra cheese", "beans", "green peppers"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f" Sorry we don't have {requested_topping} in stock at the moment")
print("\nFinished making your pizza!")
