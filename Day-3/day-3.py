# print("Welcome to the rollercoaster!")
# height = int(input("How tall are you?"))
# if height >= 120:
#     print("You can roll over!")
# else:
#     print("You can't roll over!")

# # odd or even
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"The number {num} is even")
# else:
#     print(f"The number {num} odd")

# print("Welcome to the rollercoaster!")
# height = int(input("How tall are you?"))
# if height >= 120:
#     print("You can roll over!")
#     age = int(input("How old are you?"))
#     cost = 0
#     if age > 18:
#         print("the Adult ticket costs 12$")
#         cost += 12
#     elif age > 12:
#         print("the Young ticket costs 8$")
#         cost += 8
#     else:
#         print("the Child ticket costs 5$")
#         cost += 5
#     want_ticket = input("Do you want to have a photo take? Type y for Yes and n for No")
#     if want_ticket == "y":
#         print("plus 3$")
#         cost += 3
#     print(f"Your total cost is ${cost}")
# else:
#     print("You can't roll over!")

# print("Welcome to Python Pizza deliveries!")
# size = input("What size pizza do you want? S, M or L")
# pepperoni = input("Pepperoni? Y or N")
# extra_cheese = input("Extra cheese? Y or N")
# bill = 0
# if size == "L":
#     bill += 20
# elif size == "M":
#     bill += 10
# elif size == "S":
#     bill += 5
# else:
#     print("Please enter a valid size.")
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your bill is {bill}")

print('''
 _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_| 
''')
print('Welcome to Treasure Island. Your mission is to find the treasure.')
left_right = input("Left or Right? type L or R")

if left_right == "L":
    swim_wait = input("swim or wait? type S or W")
    if swim_wait == "W":
        door = input("Which door? Red (R), Blur (B), Yellow (Y) ot something else")
        if door == "R":
            print("Burned by fire. Game Over.")
        elif door == "Y":
            print("You Win!")
        elif door == "B":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")