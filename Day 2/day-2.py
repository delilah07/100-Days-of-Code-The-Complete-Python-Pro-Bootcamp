# print(len(12345)) # Type error because int has no len() method

# print("Hello"[:]) # "Hello"
# print("Hello"[2]) # "l"
# print("Hello"[:2]) # "He"
# print("Hello"[1:4]) # "ell
# print("Hello"[-1])  # "o"
# print("Hello"[-2:-1]) # "l"

# print("123" + "345") #concatination
# print("123" + 345) #type error
# print(123 + 345) # plus sine

# print(123_456_789)
# print(len(str(123_456_789)))

# # Type Checking
# print(type("hello"))
# print(type(123))
# print(type(123.4))
# print(type(True))

# # Type Conversion
# print(float(123))
# print(float("123.2"))
# print(int(123.5))
# print(int("123"))
# print(int("abc")) # value error
# print(str(123.5))
# print(bool(123.4))
# print(bool(0.4))
# print(bool(123))
# print(bool(0))
# print(bool('hello'))
# print(bool(' '))
# print(bool(''))

# # Make this line of code without errors
# # print("number of letter in your name: " + len(input("Enter your name")))
# print("number of letter in your name: " + str(len(input("Enter your name"))))

# num = 30.854782
# print(int(num))
# print(round(num))
# print(round(num, 5))

# # f-String
# score = 0
# score += 1
# print(f'Score: {score}')

print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
print('Each person should pay: $' + str((bill+ bill * (tip/100))/people))
print(f"Each person should pay: ${(bill+ bill * (tip/100))/people}")