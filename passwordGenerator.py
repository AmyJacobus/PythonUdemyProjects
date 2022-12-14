import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your passwords: "))
nr_symbols = int(input(f"How many symbols would you like: "))
nr_numbers= int(input(f"How many numbers would you like: "))

password = ""

#Easy level
for char in range(1, nr_letters + 1):
    #generate random choice
    # random_letter = random.choice(letters)
    # password = password + random_letter
    password += random.choice(letters)

for char in range(1, nr_letters + 1):
    #generate random choice
    # random_letter = random.choice(letters)
    # password = password + random_letter
    password += random.choice(symbols)

for char in range(1, nr_letters + 1):
    #generate random choice
    # random_letter = random.choice(letters)
    # password = password + random_letter
    password += random.choice(numbers)

print("Your newly generated password is: ", password) # test


# Hard Level
password_list = []


for char in range(1, nr_letters + 1):
    #generate random choice
    # random_letter = random.choice(letters)
    # password = password + random_letter
    password_list.append(random.choice(letters))

for char in range(1, nr_letters + 1):
    #generate random choice
    # random_letter = random.choice(letters)
    # password = password + random_letter
    password_list += random.choice(symbols)


for char in range(1, nr_letters + 1):
    #generate random choice
    # random_letter = random.choice(letters)
    # password = password + random_letter
    password_list +=(random.choice(numbers))

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

