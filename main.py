import random

def generate_secret_code():
    return [random.randint(1, 6) for _ in range(4)]

def get_feedback(secret_code, guess):
    #check player's guess
    #return a list where:
    # x for incorrect digit
    # + for correct digit in the wrong position
    # o for correct digit in the correct position
    
    
    #initialize variables list
    feedback = ['x'] * 4
    secret_count = {}

    # Count occurrences of each digit in the secret code
    for digit in secret_code:
        secret_count[digit] = secret_count.get(digit, 0) + 1

    # Check for exact matches
    for i in range(4):
        if guess[i] == secret_code[i]:
            feedback[i] = 'o'
            secret_count[guess[i]] -= 1

    # Check for wrong position matches
    for i in range(4):
        if feedback[i] == 'x' and guess[i] in secret_count and secret_count[guess[i]] > 0:
            feedback[i] = '+'
            secret_count[guess[i]] -= 1
                    
    return feedback

def print_feedback(guess, feedback):
    #print the guess and its feedback as combination of o x and +
    #could be changed to colored squares for better visualization
    #and in the future, could be changed to a GUI
    color_map = {'o': '\033[42m', '+': '\033[43m', 'x': '\033[47m'}
    reset_color = '\033[0m'
    
    print()
    print()
    print("Your guess:")
    
    #add space before printing the digits
    print("           ", end="")
    
    #printing the digits
    for digit in guess:
            print("",digit,"", end=" ")
    print()
    
    #printing the feedback
    print("Feedback:")
    
    #add space before printing the feedback
    print("           ", end="")
    
    for f in feedback:
        print(f"{color_map[f]} ■ {reset_color}", end=" ")
    print()
    
def main():
    #initialize the game
    print("Welcome to Mastermind!")
    print("Try to guess the 4-digit secret code.")
    print("Digits range from 1 to 6.")
    #generate a secret code
    secret_code = generate_secret_code()
    #initialize the number of attempts
    lifes = 10 
    #launch the game
    
    while lifes > 0:
        
        #take input from the player
        print(f"\nYou have ♥ {lifes} ♥ attempts remaining.")
        guess = input(f"\nEnter your guess (4 digits from 1 to 6): ")
        
        #validate the input
        if not (len(guess) == 4 and all(num in '123456' for num in guess)):
            print("Invalid input. Please enter exactly 4 digits between 1 and 6.")
            continue
        
        #convert the string input to a list of integers
        guess = [int(num) for num in guess]
        
        #check the guess
        feedback = get_feedback(secret_code, guess)
        
        #print the feedback
        print_feedback(guess, feedback)
        
        #check if the player won
        if feedback == ['o', 'o', 'o', 'o']:
            print("Congratulations! You guessed the secret code.")
            print(f"The secret code was: {secret_code}")
            break
        
        #decrement the number of lifes
        lifes -= 1
        
    #repeat until the player wins or loses
    else:
        print("Sorry, you've used all your attempts.")
        print(f"The secret code was: {secret_code}")
    
    
if __name__ == "__main__":
    main()

