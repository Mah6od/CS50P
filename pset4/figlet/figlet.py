import sys
from pyfiglet import Figlet

def invalid():
    print("Invalid usage")
    sys.exit(1)

if len(sys.argv) != 3 or sys.argv[1] != "-f":
    invalid()

font_name = sys.argv[2]

f = input("Input: ")
figlet = Figlet(font=font_name)
print("Output: ")
print(figlet.renderText(f"{f}"))