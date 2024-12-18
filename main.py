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


