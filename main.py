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
    guess_used = [False] * 4
    secret_used = [False] * 4
    
    
    #check for exact matches
    for index in range(4):
        if guess[index] == secret_code[index]:
            feedback[index] = 'o'
            guess_used[index] = True
            secret_used[index] = True
    
    
    #check for wrong position matches        
    for index_1 in range(4):
        if feedback[index_1] == 'x':
            for index_2 in range(4):
                if not secret_used[index_2] and not guess_used[index_1]:
                    if guess[index_1] == secret_code[index_2]:
                        feedback[index_1] = '+'
                        secret_used[index_2] = True
                        break
                    
                    
    return feedback

def print_feedback(guess, feedback):
    #print the guess and its feedback as combination of o x and +
    #could be changed to colored squares for better visualization
    #and in the future, could be changed to a GUI
    
    print("Your guess:")
    
    #add space before printing the digits
    print("           ", end="")
    
    #printing the digits
    for digit in guess:
        print(digit, end=" ")
    print()
    
    #printing the feedback
    print("Feedback:")
    
    #add space before printing the feedback
    print("           ", end="")
    
    for f in feedback:
        print(f, end=" ")
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
        guess = input(f"\nYou have {lifes} attempts remaining. Enter your guess (4 digits from 1 to 6): ")
        
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

