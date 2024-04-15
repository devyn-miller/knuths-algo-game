import random
from itertools import product

def generate_random_code(pegs, slots):
    return ''.join(random.choices([str(i) for i in range(1, pegs + 1)], k=slots))

def has_won(secret_code, user_guess):
    return secret_code == user_guess

def calculate_max_unlucky_moves(pegs, slots):
    """
    Calculate the maximum number of moves required under the worst-case scenario using the minimax strategy.
    This involves simulating the game for each possible secret code and recording the number of moves taken to solve each one,
    then determining the maximum.
    """
    # This should be replaced with a calculation based on the minimax strategy
    return pegs * slots  # Placeholder for the actual calculation

def can_still_win(moves_taken, user_attempts):
    return moves_taken < user_attempts

def generate_possible_codes(slots, colors):
    return list(product(range(1, colors + 1), repeat=slots))

def calculate_feedback(code, guess):
    """
    Calculate the number of black and white pegs as feedback for a guess.
    This version is used for both manual and autonomous game modes.
    """
    black_pegs = sum(c == g for c, g in zip(code, guess))
    white_pegs = sum(min(code.count(j), guess.count(j)) for j in set(guess)) - black_pegs
    return black_pegs, white_pegs

def solve_game(pegs, slots, secret_code):
    colors = pegs  # Assuming 'pegs' represents the number of colors
    possible_codes = generate_possible_codes(slots, colors)
    attempts = 0
    while len(possible_codes) > 1:
        attempts += 1
        guess = possible_codes[0]
        print(f"Attempt {attempts}: Guess the code {guess}")
        black_pegs = int(input("Enter the number of black pegs: "))
        white_pegs = int(input("Enter the number of white pegs: "))
        feedback = (black_pegs, white_pegs)
        possible_codes = [code for code in possible_codes if calculate_feedback(code, guess) == feedback]
    return possible_codes[0], attempts

def play_manual_game(pegs, slots, secret_code):
    max_unlucky_moves = calculate_max_unlucky_moves(pegs, slots)
    print(f"The maximum number of moves if you're as unlucky as possible is: {max_unlucky_moves}")
    
    user_attempts = int(input("Enter the number of attempts you want to use to solve the game: "))
    moves_taken = 0
    history = []  # Initialize history list
    
    while moves_taken < user_attempts:
        user_guess = input("Enter your guess: ")
        moves_taken += 1
        
        red_pegs, white_pegs = calculate_feedback(secret_code, user_guess)
        history.append((user_guess, red_pegs, white_pegs))
        
        for guess, red, white in history:  # Display history
            print(f"Guess: {guess} - Red pegs: {red}, White pegs: {white}")
        
        if can_still_win(moves_taken, user_attempts):
            print("You can still guarantee a win with optimal play.")
        else:
            print("You can no longer guarantee a win with the remaining moves.")
        
        if has_won(secret_code, user_guess):
            print("Congratulations, you've cracked the code!")
            break
    else:
        print("Game over. Better luck next time!")
