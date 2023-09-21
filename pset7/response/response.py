from validator_collection import validators, checkers

def main():
    email = input("Enter an email address: ")
    try:
        if validators.email(email):
            print("Valid")
        else:
            print("Invalid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
