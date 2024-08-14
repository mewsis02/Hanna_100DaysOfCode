
# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


# Functions with more than 1 inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}? \n")


# Positional Arguments
greet_with("Hanna", "Nowhere")

# Keyword Arguments
greet_with(location="North Royalton", name="Zane")
