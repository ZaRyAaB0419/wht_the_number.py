# Function to check if the character is an alphabet
def is_alphabet(char):
    # Check if the character is an alphabet
    return char.isalpha()

# Input from the user
character = input("Enter a character: ")

# Validate input length
if len(character) == 1:
    if is_alphabet(character):
        print(f"'{character}' is an alphabet.")
    else:
        print(f"'{character}' is not an alphabet.")
else:
    print("Please enter only one character.")
