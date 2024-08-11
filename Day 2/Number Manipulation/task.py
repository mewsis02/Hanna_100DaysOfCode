
bmi = 84 / 1.65 ** 2
print(bmi)

print(round(bmi))     # rounds BMI to an integer with no decimal point numbers
print(round(bmi, 2))  # rounds BMI to 2 decimal places

# User scores a point!
score = 0
score += 1            # add 1 point to score variable
print(score)          # prints out the score variable

# F - Strings
height = 1.8
is_Winning = False
# prints out your score; height; is_Winning variables, using an F-String
print(f"Your score is {score}, You are a {height}, and You are {is_Winning}ly winning!".lower())
