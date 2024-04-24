import random
import string

def generate_password(length):
    # Define character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets based on complexity level
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password using random.choice
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Invalid length! Please enter a positive integer.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input! Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
