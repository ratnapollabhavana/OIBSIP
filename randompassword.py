
import random

# Define character sets
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "{}?@!$%^&*()_+#"

# Greeting
print("Welcome to Password Generator")

# Get user input for number of each character type
while True:
    try:
        # Prompt user for each type of character count
        n_upper = int(input("How many capital letters you want in your password?\n"))
        n_lower = int(input("How many small letters you want in your password?\n"))
        n_symbols = int(input("How many symbols you want in your password?\n"))
        n_numbers = int(input("How many numbers you want in your password?\n"))

        # Calculate total length and check if it's within the required range
        total_length = n_upper + n_lower + n_symbols + n_numbers
        if 6 <= total_length <= 16:
            break
        else:
            print("Error: The total length of your password must be between 6 and 16 characters. Please try again.")

    except ValueError:
        print("Invalid input. Please enter integer values only.")

# Generate password list with specified character types
password_list = []
for i in range(n_upper):
    password_list.append(random.choice(upper))
for i in range(n_lower):
    password_list.append(random.choice(lower))
for i in range(n_numbers):
    password_list.append(random.choice(numbers))
for i in range(n_symbols):
    password_list.append(random.choice(symbols))

# Shuffle the characters and form the password
random.shuffle(password_list)
password = ""
for char in password_list:
     password += char

# Print the final password
print("Your Generated Password is:")
print(password)

