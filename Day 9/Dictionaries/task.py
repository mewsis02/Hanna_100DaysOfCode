programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
}

# To pull out a Key from a Dictionary, It has to match the Key in the Dictionary!
# print(programming_dictionary["Bug"])

# Can be used to make an Empty Dictionary, or wipe an existing Dictionary
empty_dictionary = {}

# Can be used to add or edit an item in a Dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through a Dictionary
for key in programming_dictionary:
    print(f"The {key} is {programming_dictionary[key].lower()}.")
