#we are going to slicing a list 
cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
#we can slice the list to get a portion of it
print(cars[1:4])  # This will print elements from index 1 to 3 (not including index 4)prin
print(f"There are the cars present at the auction:{cars[-3:]}")
for car in cars[2:]:
    print(f"{car} ia an affordable car")

#we can also slice the list to get a portion of it