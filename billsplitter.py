import random


# prompt user for no of friends
noOfFriends = int(input("Enter the number of friends joining (including you): \n"))
# check if user prompted desired result(number) or not
if noOfFriends > 0:
    pass
else:
    print("No one is joining for the party")
    exit()

# store the friends name in a list and convert it into dictionary as a key.
friendsName = []

print("Enter the name of every friend (including you), each on a new line:")
for name in range(noOfFriends):
    friendsName.append(input())

# Total bill and splitting it equally
totalBill = int(input("Enter the total bill value: \n"))

friendsList = dict.fromkeys(friendsName, 0)

# prompt users for a Lucky winner!
luckyWinner = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: \n")

# printing lucky winner's name
if luckyWinner == "Yes":
    lucky = random.choice(friendsName)
    print(f"{lucky} is the lucky one!")
    equalSplit = round(totalBill / (noOfFriends - 1), 2)
# Payment need to be give by each user, final output with lucky winner
    friendsList = dict.fromkeys(friendsName, equalSplit)
    friendsList[lucky] = 0
else:
    print("No one is going to be lucky")
    equalSplit = round(totalBill / noOfFriends, 2)
# Payment need to be give by each user, final output without lucky winner
    friendsList = dict.fromkeys(friendsName, equalSplit)

print(friendsList)



