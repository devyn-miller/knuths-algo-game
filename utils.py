import random
from itertools import product

def generate_random_code(pegs, slots):
    return ''.join(random.choices([str(i) for i in range(1, pegs + 1)], k=slots))

def has_won(secret_code, user_guess):
    return secret_code == user_guess

def calculate_max_unlucky_moves(pegs, slots):
    # This is a simplified estimation. The actual calculation can be more complex based on game rules.
    return pegs * slots

def can_still_win(moves_taken, user_attempts):
    return moves_taken < user_attempts
