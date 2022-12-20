import random
import string

def generate_password(length):
    # Generate a random sequence of characters
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

def main():
    # Prompt the user for the password length
    length = int(input("Enter the desired password length: "))
    # Generate and print the password
    password = generate_password(length)
    print(f"Your password is: {password}")

if __name__ == '__main__':
    main()