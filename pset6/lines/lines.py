import sys

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            code_lines = sum(1 for line in file if line.strip() and not line.lstrip().startswith("#"))
            return code_lines
    except FileNotFoundError:
        sys.exit("File not found!")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]
    lines_count = count_lines(filename)
    print(f"Lines of code in {filename}: {lines_count}")
