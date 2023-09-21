def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    try:
        # Remove any leading "$" or spaces, then convert to float
        d = d.replace('$', '').strip()
        return float(d)
    except ValueError:
        print("Invalid input. Please enter a valid dollar amount.")
        exit(1)

def percent_to_float(p):
    try:
        # Remove any "%" symbol, then convert to float
        p = p.replace('%', '')
        return float(p) / 100.0  # Convert percentage to decimal
    except ValueError:
        print("Invalid input. Please enter a valid percentage.")
        exit(1)

main()