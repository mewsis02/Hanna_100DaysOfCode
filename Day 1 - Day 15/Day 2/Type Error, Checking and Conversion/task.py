
# Stores the string "12345" into a new variable called number
number = "12345"

# Prints out the length and data type of the number variable
print(len(number))
print(type(number))
print("")

# Prints out the 4 Data Types (w/ Examples of Each)
print(type("Hello Hanna"))
print(type(21))
print(type(19.2345678))
print(type(True))
print("")

# Type Conversion
print("123" + "456")  # string concatenation
print(int("123") + int("456"))  # treats them as integers, and adds them together
print("")

name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_name))
