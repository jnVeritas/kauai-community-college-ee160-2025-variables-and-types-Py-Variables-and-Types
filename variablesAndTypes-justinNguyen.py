# AMDG

#
# Developer: Justin Nguyen
# Last Edited: 05/14/2025
# Created: 05/10/2025
# Description: It checks the number of characters in a user-inputted text and whether it has met a ideal goal or tolerable goal.
#

# Some of the variables are defined here. More will be defined later.
characterGoal = 10000
allowedErrorPercent = 3
curNumCharacters = 0
greeting = "hello"
greeted = "world"
badCharacterGoal = False
# This final variable is a bonus feature, and it'll be used later on.

# This block of code prints out an introduction.
print("")
print(greeting + " " + greeted + "!") # If another operation was used, the program would return "TypeError: unsupported operand type(s) for X: 'str' and 'str,'" with X being the operation used. For multiplication, it returns "TypeError: can't multiply sequence by non-int of type 'str.'"
print("I am a Character Count Checker, but you can call me Cece for short!")
print("Please tell me the number of characters you want to check for:")
# The "hello world!" message is printed in this.

# This should set the character goal to whatever integer the user types in.
while True:
    try:
        characterGoal = int(input())
        break
    except ValueError:
        print("Please try again, with an integer value.")
# If the user decides to not set an integer value, they would have to redo.

# This block ensures the character goal isn't theoretically impossible, though it would still be possible for the user to set the goal to a practically impossible-to-reach number.
if characterGoal <= 0:
    print("Okay, so I won't let you have a goal of " + str(characterGoal) + " characters. So now, your character goal is now 10000.")
    characterGoal = characterGoal * 0 + 10000
    badCharacterGoal = True
    print("")
# The program sets the character goal to 10000, which is a value given in the original assignment. It also stores the fact that the user tried to set an irrational goal for later.

print("Please enter how far below from this goal you're willing to be (%):")

# This block will get the user input and set it as the allowed error value.
while True:
    try:
        allowedErrorPercent = float(input())
        break
    except ValueError:
        print("Please try again, with an numeric value.")
# It will continue trying again if the user does not give an actual number.

# This sets the error percentage to a value of three as given in the assignment, as setting it to one hundred or more would not be desirable.
if allowedErrorPercent >= 100:
    if not badCharacterGoal:
        print("Okay, you're telling me to just disregard the original character count? Here, your error percent is now 3.")
    else:
        print("First, you try to have a nonexistent character goal. Now, you're saying to disregard the character goal? Why are you even using this program? Here, let me set your error percent to 3.")
    allowedErrorPercent = 3
    print("")
# This undesirability comes from two points: that an error of 100 percent means dividing by zero later and having it be more is unreasonable.

allowedCharacters = int(characterGoal - characterGoal * allowedErrorPercent * 0.01)

print("Please type/paste your text below:")

# In this block, more variables are defined for future uses.
curNumCharacters = len(input())
percentCompleted = curNumCharacters / characterGoal * 100 # Previous lines of code made sure that we don't divide by zero for this line and the next.
percentFromAllowed = (allowedCharacters - curNumCharacters) / allowedCharacters * 100 # as the error would say "ZeroDivisionError: division by zero."
distanceFromCompletion = abs(characterGoal - curNumCharacters)
# This includes the length of the user's text in characters.

print("")

greeting = "Hi!"

# This block checks if the ultimate character count has been met or not and if the point of allowed error has been passed, if needed.
if percentCompleted < 100.0:
    if curNumCharacters >= allowedCharacters:
        print(greeting + " You typed " + str(curNumCharacters) + " characters or " + str(float(curNumCharacters)) +" characters in decimal form, which is " + str(percentCompleted) + "% of the character goal which is " + str(distanceFromCompletion) + " characters away. You did meet your acceptable goal though.") # If the string was a float, the error message would be "ValueError: could not convert string to float: 'Hi!'"
    else:
        print("You typed " + str(curNumCharacters) + " characters, which is " + str(percentCompleted) + "% of the character goal. You are still " + str(percentFromAllowed) + "% away from the tolerable goal and " + str(distanceFromCompletion) + " characters away from your official goal.")
else:
    print("Congratulations! You met your character goal, writing a total of " + str(curNumCharacters) + " characters which is " + str(distanceFromCompletion) + " characters more than the goal.")
# There is no need for another nested if statement because meeting the ultimate character goal also means passing the point of error.
