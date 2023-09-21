import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Use regular expression to find all occurrences of "um" as a separate word
    um_matches = re.findall(r'\bum\b', s, re.IGNORECASE)

    # Return the count of "um" matches
    return len(um_matches)

if __name__ == "__main__":
    main()
