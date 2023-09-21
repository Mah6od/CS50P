def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the plate meets all requirements
    return has_valid_length(s) and starts_with_letters(s) and no_middle_numbers(s) and no_punctuation(s)

def has_valid_length(s):
    # Check if the length of the plate is between 2 and 6 characters
    return 2 <= len(s) <= 6

def starts_with_letters(s):
    # Check if the plate starts with at least two letters
    return s[:2].isalpha()

def no_middle_numbers(s):
    # Check if numbers are only allowed at the end, and the first number is not '0'
    if len(s) == 2:
        return True  # Handles cases with only two characters, e.g., "NR"
    return s[2:].isdigit() and (len(s) == 2 or s[2] != '0')

def no_punctuation(s):
    # Check if there are no periods, spaces, or punctuation marks in the plate
    return all(char.isalnum() for char in s)

if __name__ == "__main__":
    main()
