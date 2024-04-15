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

def calculate_feedback(secret_code, user_guess):
    red_pegs = sum(a == b for a, b in zip(secret_code, user_guess))
    white_pegs = sum(min(secret_code.count(j), user_guess.count(j)) for j in set(secret_code)) - red_pegs
    return red_pegs, white_pegs

def minimax_strategy(pegs, slots):
    """
    Implement the minimax strategy for Mastermind, adapted for different numbers of pegs and colors.
    This function should generate all possible codes, make a strategic first guess, and then apply the minimax principle.
    """
    # Placeholder for the actual implementation
    pass

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
