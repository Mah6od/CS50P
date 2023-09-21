def main():
    user_input = input("Input: ").strip()
    text_without_vowel = shorten(user_input)

    print("Output:",text_without_vowel)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    shortened = []
    for w in word:
        if w.casefold() not in vowels:
            shortened.append(w)
    output = str("".join(shortened))
    return output

if __name__ == "__main__":
    main()