camelCase = input("camelCase: ").strip()
snake_case = ""

for char in camelCase:
    if char.isupper():
        snake_case += "_" + char.lower()

    else:
        snake_case += char

snake_case = snake_case.lstrip("_")
print("Snake_Case:", snake_case)