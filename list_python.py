#Today we would talking about lists in python
#Lists are used to store multiple items in a single variable.
#Lists are created using square brackets [] and can contain items of different data types.
print("LIsts are used to store multiple items in a sngle variable")
friends = ["Maxwell", "rahcel", "adeola", "Timilehin"]
print(friends)
print(friends[0])  # Accessing the first item in the list
print(friends[1]) #Acessing the second item in the list 
print(friends[2].title()) #Acessing the third item on the lsit and capitalizng the first letter  of the letter 

text = f"My first friend in the university of ibadan is {friends[-1].upper()}"
print(text)  # Accessing the last item in the list and converting it to uppercase
#changing the value of an item in the lsit and also adding and removing items on the list 
friends[2] = "john" # i assigned the third spot in the list to a new variable 
print(friends)  # Printing the updated list
friends.append("joy") #Adding a new item to the end of the list instead of replacing with the old one 
print(friends)  # Printing the updated list after adding a new item
friends.insert(-2, "titilayo")
print(friends)  # Printing the updated list after inserting a new item
del friends[-4]
print(friends)  # Printing the updated list after deleting an item
#pop method removes the last item in the list and returns it
popped_friend = friends.pop()  # Removing the last item from the list
print(friends)  # Printing the updated list after popping the last item
print(f"The popped friend in the list is {popped_friend.upper()}")
#removing an item from the list using the remove method
friends.remove("Maxwell")  # Removing a specific item from the list
print(friends)

#Sorting the list in alphabetical order
cars = ["bmw", "audi", "toyota", "subaru"]
# cars.sort()  # Sorting the list in alphabetical order
# print(cars) # Printing the sorted list
# #Sorting the list in reverse order
# cars.sort(reverse= True)  # Sorting the list in reverse alphabetical order
# print(cars)  # Printing the sorted list in reverse order
#Sorting the list temporarily
print("Here is the origibnal list of cars.")
print(cars)
print("Here is the sorted list of cars")
print(sorted(cars))  # Printing the sorted list temporarily
cars.reverse()
print("Here is the list of cars in reverse order")
print(cars)
#finding the length of the list 
number_of_cars = len(cars)  # Finding the length of the list
print(f"The number of the list of cars is {number_of_cars}")