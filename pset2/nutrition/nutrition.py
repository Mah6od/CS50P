def main():
    # Define a dictionary to store fruit names and their calories
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
        "bananas": 105,
        "blackberries": 30,
        "blueberries": 85,
        "cantaloupe": 55,
        "cherries": 50,
        "cranberries": 5,
        "grapefruit": 52,
        "grapes": 69,
        "honeydew melon": 64,
        "kiwifruit": 90,
        "lemons": 17,
        "limes": 20,
        "mango": 150,
        "oranges": 62,
        "peaches": 59,
        "pear": 100,
        "persimmons": 81,
        # Add more fruits and their calorie information here
    }

    # Prompt the user for a fruit (case-insensitively)
    fruit = input("Enter a fruit: ").lower()

    # Look up the fruit in the dictionary and display its calories
    if fruit in fruit_calories:
        calories = fruit_calories[fruit]
        print(f"Calories: {calories}")
    else:
        print("")

if __name__ == "__main__":
    main()
