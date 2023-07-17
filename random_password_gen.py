import random
import sys

choice = 0


def check_length(user_input):
    if user_input.isdigit() and (len(user_input) >= 1 and len(user_input) <= 3):
        return int(user_input)

    print("Invalid input.")
    sys.exit()


def check_choice(user_input):
    if user_input.isdigit() and len(user_input) == 1:
        if user_input >= "1" and user_input <= "3":
            return int(user_input)

    print("Invalid input.")
    sys.exit()


# Example usage


random_list = []
password = ""
length = str(sys.argv[1])
length = check_length(length)
choice = str(sys.argv[2])
choice = check_choice(choice)
if choice == 1:
    for i in range(0, length):
        random_number = random.randint(65, 90)
        random_list.append(random_number)
        random_number = random_list.append(random_number)
        random_number = random.randint(97, 122)
        random_list.append(random_number)
        random_element = random.choice(random_list)
        password = password + chr(random_element)
elif choice == 2:
    for i in range(0, length):
        random_number = random.randint(65, 90)
        random_list.append(random_number)
        random_number = random.randint(97, 122)
        random_list.append(random_number)
        random_number = random.randint(48, 57)
        random_list.append(random_number)
        random_element = random.choice(random_list)
        password = password + chr(random_element)

elif choice == 3:
    for i in range(0, length):
        random_number = random.randint(65, 90)
        random_list.append(random_number)
        random_number = random.randint(97, 122)
        random_list.append(random_number)
        random_number = random.randint(33, 47)
        random_list.append(random_number)
        random_number = random.randint(48, 57)
        random_element = random.choice(random_list)
        password = password + chr(random_element)
print("              ")
print("Password : ", password)
print("              ")
