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
    
    #check for exact matches

    #check for wrong position matches        
    print(" ")

def print_feedback(guess, feedback):
    #print the guess and its feedback as combination of o x and +
    #could be changed to colored squares for better visualization
    #and in the future, could be changed to a GUI
    print("Your guess:")
    
    
    
def main():
    #initialize the game
    #generate a secret code
    #initialize the number of attempts
    #launch the game
    #take input from the player
    #check the guess
    #print the feedback
    #check if the player won
    #check if the player lost
    #repeat until the player wins or loses
    print("Welcome to Mastermind!")


