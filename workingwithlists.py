#we would be starting with for loops
#first we create a list of guys i know then we would loop through them one by one one\
guys = ["Maxwell", "rahcel", "adeola", "Timilehin"]
for guy in guys:
    print(f"Hello {guy.lower()}, you have been chosen as one of my closet friends")
    #we would be using the .lower() method to convert the string to lowercase
magicians = ["David Blaine", "Dynamo", "Criss Angel", "Penn and Teller"]
for magician in magicians:
    print(f"{magician.title()} is a great magician")
    print(f"I can't wait to see {magician.title()} perform his magic tricks")