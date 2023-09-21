from fractions import Fraction

def main():
    while True:
        fraction_str = input("Fraction: ")

        try:
            fraction = Fraction(fraction_str)  # Parse the input as a fraction

            if fraction.denominator == 0:
                raise ZeroDivisionError

            percentage = round(float(fraction) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break  # Exit the loop if input is valid
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction (X/Y).")

if __name__ == "__main__":
    main()
