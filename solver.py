import random
from itertools import product

def generate_random_code(pegs, slots):
    return ''.join(random.choices([str(i) for i in range(1, pegs + 1)], k=slots))

def has_won(secret_code, user_guess):
    return secret_code == user_guess

def calculate_max_unlucky_moves(pegs, slots):
    """
    Estimates the maximum number of moves to solve the Mastermind game in the worst-case scenario.
    This is a heuristic based on known results for standard configurations and may not accurately reflect
    the maximum for all possible configurations.
    
    Known results:
    - For a classic game (6 colors, 4 slots), the maximum is 5 moves (Knuth's algorithm).
    - This function extrapolates from the classic game's result for simplicity.
    
    Args:
    - pegs (int): The number of different pegs (colors) available.
    - slots (int): The number of slots in the game.
    
    Returns:
    - int: An estimated maximum number of moves.
    """
    # This is a simplified heuristic. For the classic game configuration, Knuth's algorithm guarantees a solution in 5 moves or fewer.
    if pegs == 6 and slots == 4:
        return 5
    # For other configurations, we provide a simplified estimation. This should be replaced with a more accurate calculation if available.
    return min(5 + (slots - 4), pegs)  # Simplified and arbitrary heuristic for educational purposes.

def can_still_win(moves_taken, user_attempts):
    return moves_taken < user_attempts
