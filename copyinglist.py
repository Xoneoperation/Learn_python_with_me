#we are going to be copying a list 
print("Here are different types of cars:")
cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
#we can copy the list to get a portion of it
french_cars = cars[:3]
print(f"\nThese are good example of {french_cars} in the cars listed above")
#we want to prove that they are different lists
cars.append("Peugeot")
french_cars.append("Renault")
print(f"\nThe original list of cars is: {cars}")
print(f"\nThe copied list of cars is: {french_cars}")