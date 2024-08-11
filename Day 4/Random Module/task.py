
import random

# Gets a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(f"My random integer is... {random_integer}")

# Gets a random float between 0 and 10
random_float = random.random() * 10
print(random_float)

print("")
# Heads OR Tails - IF < 0.5: Heads, IF >= 0.5: Tails
heads_or_tails = random.random()
print(heads_or_tails)
if heads_or_tails < 0.5:
    print("Heads")
elif 0.5 <= heads_or_tails < 1:
    print("Tails")
