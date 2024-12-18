import random
import pygame
import sys

def generate_secret_code():
    """Generate a secret code of 4 digits chosen randomly from 1 to 6."""
    return [random.randint(1, 6) for _ in range(4)]

def get_feedback(secret_code, guess):
    """Provide feedback on the player's guess.
    Returns a list where:
    - 'green' indicates a correct digit in the correct position.
    - 'yellow' indicates a correct digit in the wrong position.
    - 'gray' indicates an incorrect digit.
    """
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

def draw_feedback(screen, guess, feedback, attempt):
    """Display the guess and feedback on the screen."""
    font = pygame.font.Font(None, 74)
    colors = {'o': (0, 255, 0), '+': (255, 255, 0), 'x': (255, 0, 0)}

    # Display guess
    for i, digit in enumerate(guess):
        text = font.render(str(digit), True, (0, 0, 0))
        screen.blit(text, (50 + i * 100, 50 + attempt * 150))

    # Display feedback
    for i, color in enumerate(feedback):
        pygame.draw.rect(screen, colors[color], pygame.Rect(50 + i * 100, 120 + attempt * 150, 40, 40))

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Mastermind")

    font = pygame.font.Font(None, 50)
    clock = pygame.time.Clock()

    secret_code = generate_secret_code()
    attempts = 10
    attempt = 0
    guesses = []
    feedbacks = []
    input_guess = []

    running = True
    while running:
        screen.fill((255, 255, 255))

        # Display instructions
        instructions = font.render("Enter digits (1-6) and press Enter", True, (0, 0, 0))
        screen.blit(instructions, (50, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(input_guess) == 4:
                    guesses.append(input_guess)
                    feedback = get_feedback(secret_code, input_guess)
                    feedbacks.append(feedback)
                    if feedback == ['green', 'green', 'green', 'green']:
                        print("Congratulations! You guessed the secret code.")
                        print(f"The secret code was: {''.join(map(str, secret_code))}")
                        running = False
                    attempt += 1
                    input_guess = []
                    if attempt >= attempts:
                        print("Sorry, you've used all your attempts.")
                        print(f"The secret code was: {''.join(map(str, secret_code))}")
                        running = False
                elif event.key == pygame.K_BACKSPACE and input_guess:
                    input_guess.pop()
                elif event.unicode.isdigit() and len(input_guess) < 4 and 1 <= int(event.unicode) <= 6:
                    input_guess.append(int(event.unicode))

        # Draw previous guesses and feedbacks
        for i in range(len(guesses)):
            draw_feedback(screen, guesses[i], feedbacks[i], i)

        # Draw current input
        for i, digit in enumerate(input_guess):
            text = font.render(str(digit), True, (0, 0, 0))
            screen.blit(text, (50 + i * 100, 50 + attempt * 150))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
