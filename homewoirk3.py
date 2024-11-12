def is_alphabet(char):
    if char.isalpha():
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")

# Example usage
character = input("Enter a character: ")
is_alphabet(character)
