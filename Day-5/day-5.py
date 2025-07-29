# fruits = ['apple', 'banana', 'pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + ' pie')
# print(fruits)

# score = [125, 25, 87, 130, 102, 75, 94]
# total_score_using_sum = sum(score)
# print(total_score_using_sum)
# total_score = 0
# for num in score:
#     total_score += num
# print(total_score)

# max_score_using_max = max(score)
# print(max_score_using_max)
# max_score = 0
# for num in score:
#     max_score = num if num > max_score else max_score
# print(max_score)

# for number in range(1, 10) # from 1 to 9
# for number in range(1, 10, 3) # from 1 to 9 with step 3 - 1, 4, 7

# total = 0
# for num in range(1, 101):
#     total += num
# print(total)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password_str = ''
# for char in range(1, nr_letters + 1):
#     password_str += random.choice(letters)
# for sym in range(1, nr_symbols + 1):
#     password_str += random.choice(symbols)
# for num in range(1, nr_numbers + 1):
#     password_str += random.choice(numbers)
# print(password_str)

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for sym in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ('').join(password_list)
print(password)