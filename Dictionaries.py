#Let's dive into dictionaries in python
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered, changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and they have keys and values.

alien_O = {"color": "green", "points": 5}
print(alien_O["color"])
new_points = alien_O["points"]
print(f"You just earned {new_points} points!")
alien_O['z_position'] = 0
alien_O['y_position'] = 25
alien_O['x_position'] = 35
print(alien_O)
alien_1 = {}
alien_1['height'] = 5
alien_1['weight'] = 10
alien_1['age'] = 100
print(alien_1)

#modifying the values of a key in a dictionary
alien_1['height'] = 50
alien_1['weight'] = 100
print(alien_1)
# so we want to mimic the movement of an alien in a game
alien_O['speed'] = 'medium'
print(f"original position of the alien is {alien_O['x_position']}")
if alien_O['speed'] == 'slow':
    x_increment = 1     
elif alien_O['speed'] == 'medium':
    x_increment =  2
else:
    x_increment = 3
alien_O['x_position'] = alien_O['x_position'] + x_increment
print(f"The new position of the alien is {alien_O['x_position']}")
#removing a key-value pair from a dictionary
del alien_O['z_position']
print(alien_O)
favorite_languages = {
    'demola' : 'python',
    'isaac'  : 'javascript',
    'abuka'  : 'C#',
    'joy'    : 'java',
}
print(f"Demola's favorite  programming language is {favorite_languages['demola']}")

#looping through a dictionary 
user_O = {
    'username' : ' Ademsarts54',
    'First'    : 'Ademola',
    'Last'     : 'Gbadero'
}
for key, value in user_O.items():
    print("\nkey " + key)
    print("\nvalue "  + value)
    for k, v in user_O.items():
        print(f"Key: {k}, Value: {v}")
friends =  ['joy', 'shola']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f"Hi,{name} , Looks like your favourite language is {favorite_languages[name].title()}")

#now we go in and go ahead to nesting dictionaries \
aliens_0 = {'color': 'green', 'points': 5}
aliens_1 = {'color': 'yellow', 'points': 10}
aliens_2 = {'color': 'red', 'points': 15}
aliens = [aliens_0, aliens_1, aliens_2]
for alien in aliens:
    print(alien)
#making an empty list of aliens
aliens_3 = []
#make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5}
    aliens_3.append(new_alien)
for alien in aliens_3[:5]:
    print(alien)

#A list in a dictionary 
