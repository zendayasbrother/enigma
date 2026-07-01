def welcome_message():
    name = input("Enter your name: ")
    print("Welcome", name, "to this adventure!")

def choose_path():
    answer = input("You are on a dirt road as a 20-year-old. It has come to an end, and you can either go left or right. Which way would you go? ").lower()
    if answer == "left":
        return left_path()
    elif answer == "right":
        return right_path()
    else:
        print("Not a valid option. You lose")

def left_path():
    answer = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ")
    if answer == "swim":
        return swim_path()
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You lost.")
        return False
    else:
        print("Not a valid option. You lose")
        return False

def swim_path():
    answer = input("You're now in the forest and you've been walking for five minutes. You reach a Y junction. The left path has a continuing path that has this mysterious ball of light at the end of it, and the right path is the start of a hilly path to what you hope is a campsite. Type 'left' or 'right' to continue: ")
    if answer == "left":
        # Left path continuation
        print("You chose to follow the mysterious light. What awaits you ahead?")
        return True
    elif answer == "right":
        # Right path continuation
        return right_path_continuation()
    else:
        print("Not a valid option. You lose")
        return False

def right_path():
    answer = input("You see an abandoned dirt bike on your walk. It looks fairly new and functional. Would you take it to get to the campsite quicker or would you not risk potentially stealing? Type 'bike' or 'safe' to continue: ")
    if answer == "bike":
        return bike_path()
    elif answer == "safe":
        return safe_path()
    else:
        print("Not a valid option. You lose")
        return False

def bike_path():
    answer = input("You have now reached the quarter point. You're about to take a break after no food for four hours. But suddenly, you hear the loudest growl from some direction. Do you panic and quickly restart the dirt bike or do you assume it's harmless and continue eating your cereal bar? Type 'restart' or 'harmless' to continue: ")
    if answer == "restart":
        return restart_path()
    elif answer == "harmless":
        return harmless_path()
    else:
        print("Not a valid option. You lose")
        return False

def right_path_continuation():
    answer = input("You're escaping the growl and you see a speed limit sign with a 20 on it. Are you going to speed to not risk hearing the growl, or go below 20 for the rest of the bike ride? Type 'over' or 'under' to continue: ")
    if answer == "over":
        # Continue right path with speeding
        print("You chose to speed up. What's next?")
        return True
    elif answer == "under":
        # Continue right path with cautious speed
        print("You chose to maintain a slow speed. What's next?")
        return True
    else:
        print("Not a valid option. You lose")
        return False

def safe_path():
    answer = input("You can't see the other campsite in your direction on your map. Suddenly, you see some teenage bikers come your way. Are you going to ask the teens for help or figure this out on your own until you can't? Type 'teens' or 'independence' to continue: ")
    if answer == "teens":
        # Seek help from teens
        print("You chose to ask for help from the teens. What will they advise?")
        return True
    elif answer == "independence":
        # Continue independently
        print("You chose to continue on your own. Can you find the campsite?")
        return True
    else:
        print("Not a valid option. You lose")
        return False

# Define other paths and outcomes similarly...

def main():
    welcome_message()
    if choose_path():
        print("Congratulations! You successfully navigated through the adventure.")
    else:
        print("Game Over")

main()