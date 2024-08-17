
from art import logo
print(logo)


def add(n1, n2):
    """adds two numbers together"""
    return n1 + n2


def subtract(n1, n2):
    """subtracts the 2nd number from the 1st number"""
    return n1 - n2


def multiply(n1, n2):
    """multiplies two numbers together"""
    return n1 * n2


def divide(n1, n2):
    """divides the first number by the second number"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

display_operations = ""
for each_operation in operations:
    display_operations += f" {each_operation} "

run_calculator = True
while run_calculator:
    print("\n")
    base_number = float(input("What is your first number? "))

    keep_calculating = True
    while keep_calculating:
        new_operation = input(f"Which Operation ({display_operations})? ")
        second_number = float(input("What is your next number? "))
        answer = operations[new_operation](base_number, second_number)
        if new_operation == "-" and second_number < 0:
            second_number -= (second_number + second_number)
            new_operation = "+"
        if new_operation == "+" and second_number < 0:
            second_number -= (second_number + second_number)
            new_operation = "-"
        print(f"\n{base_number} {new_operation} {second_number} = {answer}")
        base_number = answer

        yes_or_no = ""
        while yes_or_no != "yes/no":
            yes_or_no = input(f"Keep calculating with {answer}, or not? yay, nay, or quit? ").lower()
            if yes_or_no == "nay":
                yes_or_no = "yes/no"
                keep_calculating = False
            elif yes_or_no == "yay":
                yes_or_no = "yes/no"
                keep_calculating = True
            elif yes_or_no == "quit":
                yes_or_no = "yes/no"
                keep_calculating = False
                run_calculator = False
            else:
                print("\nThat is an invalid answer.")
print("Goodbye For Now :3")
