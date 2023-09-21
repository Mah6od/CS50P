import inflect

# Initialize the inflect engine
p = inflect.engine()

# Initialize a list to store names
names = []

# Prompt the user for names until they input Control-D (EOF)
try:
    while True:
        name = input("Enter a name (or press Control-D to finish): ")
        names.append(name)

except EOFError:
    pass

# Determine the number of names and format the farewell message accordingly
num_names = len(names)
farewell = "Adieu, adieu, to "

if num_names == 1:
    farewell += names[0]
elif num_names == 2:
    farewell += names[0] + " and " + names[1]
else:
    farewell += ", ".join(names[:-1]) + ", and " + names[-1]

# Print the formatted farewell message
print(farewell)
