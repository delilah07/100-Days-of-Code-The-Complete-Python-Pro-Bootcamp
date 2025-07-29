import random
# import my_module

# random_int = random.randint(1, 10)
# print(random_int)

# print(my_module.my_favourite_number)

# random_from_0_to_1 = random.random()
# random_from_1_to_10 = random.random() * 10
# print(random_from_0_to_1)
# print(random_from_1_to_10)

# random_float = random.uniform(5, 55)
# print(random_float)

# #  Heads or Tails
# random_from_0_to_1 = random.random()
# if random_from_0_to_1 > 0.5:
#     print("Heads")
# else:
#     print('Tails')

# # LIST
# fruits = ['apple', 'banana', 'pineapple', 'pear']
# print(fruits[0])
# print(fruits[-1])
# print(fruits[10])

# fruits[1] = 'grapes'
# fruits.append('morela')
# fruits[len(fruits):] = (['blueberry']) # the same as .append
# fruits.extend(['melon', 'cherry'])
# print(fruits)

# friends=['Alice', 'Bob', 'Tom', "David"]
# # 1st option
# random_index = random.randint(1, len(friends))
# print(friends[random_index - 1])
# # 2nd option
# print(random.choice(friends))

# # Nested List
# names = ['Alice', 'Bob', 'Tom', "David", 'Marry']
# man_names = [ 'Bob', 'Tom', "David", ]
# woman_names = ['Alice',  'Marry']
# names = [man_names, woman_names]
# print(names)

# # Rock, Paper or Scissors
play = ['Rock', 'Paper', 'Scissors']
user_choice = int(input('Choose Rock (0), Paper (1) or Scissors (2)'))
comp_choice = random.choice(play)

if play[user_choice] == comp_choice:
    print(f'You and computer chose {play[user_choice]}. Noone is loose')
elif play[user_choice] == 'Rock':
    if comp_choice == "Paper":
        print(f'You chose {play[user_choice]} and computer chose {comp_choice}.Computer wins')
    elif comp_choice == 'Scissors':
        print(f'You chose {play[user_choice]} and computer chose {comp_choice}. You win')
elif play[user_choice] == 'Paper':
    if comp_choice == "Rock":
        print(f'You chose {play[user_choice]} and computer chose {comp_choice}. You win')
    elif comp_choice == 'Scissors':
        print(f'You chose {play[user_choice]} and computer chose {comp_choice}. Computer wins')
elif play[user_choice] == 'Scissors':
    if comp_choice == "Rock":
        print(f'You chose {play[user_choice]} and computer chose {comp_choice}. Computer wins')
    elif comp_choice == 'Paper':
        print(f'You chose {play[user_choice]} and computer chose {comp_choice}. You win')
else:
    print('You chose something else')