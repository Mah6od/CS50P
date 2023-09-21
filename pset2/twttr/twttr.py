def remove_vowel(text):
    vowels = ("AEIOUaeiou")

    text_without_vowel = ""

    for char in text:
        if char not in vowels:
            text_without_vowel += char

    return text_without_vowel

def main():
    user_input = input("Input: ").strip()
    text_without_vowel = remove_vowel(user_input)

    print("Output:",text_without_vowel)

if __name__ == "__main__":
    main()