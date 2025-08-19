#we  are working on a guest list working with lists in python
guest_list = ["Timilehin", "Adeola", "Rachel", "Maxwell", "Titilayo"]
messsage1 = f"Hello {guest_list[0]}, you are invited to my birthday party!"
messsage2 = f"Hello {guest_list[1]}, you are invited to my birthday party!"
messsage3 = f"Hello {guest_list[2]}, you are invited to my birthday party!"
messsage4 = f"Hello {guest_list[3]}, you are invited to my birthday party!"
messsage5 = f"Hello {guest_list[4]}, you are invited to my birthday party!"
print(messsage1)
print(messsage2)
print(messsage3)
print(messsage4)
print(messsage5)
missing_guest =  f"As it looks {guest_list[1]} won't be able to make it to the party"
print(missing_guest)
guest_list[1] = "Joy"
#The missing guest has been replaced with a new guest, now we will send out her own invitation
messsage2 = f"Hello {guest_list[1]}, you are invited to my birthday party!"
print(messsage2)
#now we print all the guests list again and their invitaition
messsage1 = f"Hello {guest_list[0]}, you are invited to my birthday party!"
messsage2 = f"Hello {guest_list[1]}, you are invited to my birthday party!"
messsage3 = f"Hello {guest_list[2]}, you are invited to my birthday party!" 
messsage4 = f"Hello {guest_list[3]}, you are invited to my birthday party!"
messsage5 = f"Hello {guest_list[4]}, you are invited to my birthday party!"
print(messsage1)
print(messsage2)
print(messsage3)
print(messsage4)
print(messsage5)
print("I have found a bigger table, so I will invite more people to the party")
guest_list.insert(0,"John")
guest_list.insert(3, "Joy")
guest_list.append("Nelson")
#Now we will print the new guest list and their invitation
messsage1 = f"Hello {guest_list[0]}, you are invited to my birthday party!"
messsage2 = f"Hello {guest_list[1]}, you are invited to my birthday party!"
messsage3 = f"Hello {guest_list[2]}, you are invited to my birthday party!"
messsage4 = f"Hello {guest_list[3]}, you are invited to my birthday party!"
messsage5 = f"Hello {guest_list[4]}, you are invited to my birthday party!"
messsage6 = f"Hello {guest_list[5]}, you are invited to my birthday party!"
messsage7 = f"Hello {guest_list[6]}, you are invited to my birthday party!"
print(messsage1)
print(messsage2)
print(messsage3)
print(messsage4)
print(messsage5)
print(messsage6)
print(messsage7)

#Now we will be shrinking the guest list
print("Unfortunately, I can only invite two people to the party")
removed_guest = guest_list.pop()
print(f"Sorry {removed_guest}, you are no longer invited to the party")
removed_guest = guest_list.pop()
print(f"Sorry {removed_guest}, you are no longer invited to the party")
removed_guest = guest_list.pop()
print(f"Sorry {removed_guest}, you are no longer invited to the party")
removed_guest = guest_list.pop()
print(f"Sorry {removed_guest}, you are no longer invited to the party")
removed_guest = guest_list.pop()
print(f"Sorry {removed_guest}, you are no longer invited to the party")
removed_guest = guest_list.pop()
print(f"Sorry {removed_guest}, you are no longer invited to the party")
#Now we will print the remaining guests
print(f"The remaining guests are: {guest_list}")
assurance_message1 = f"{guest_list[0]}, you are still invited to the party"
assurance_message2 = f"{guest_list[1]}, you are still invited to the party"
print(assurance_message1)
print(assurance_message2)
del guest_list[0]
del guest_list[0]
print(guest_list)
#Now we will print the final guest list