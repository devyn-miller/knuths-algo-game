import pytest
from solver import solve_game, calculate_max_unlucky_moves

@pytest.mark.parametrize("pegs,slots,expected_max_moves", [
    (6, 4, 5),  # Classic game configuration
    (3, 3, 4),  # Example heuristic result for smaller configuration
    (5, 4, 5),  # Another configuration, assuming a heuristic result
    (7, 4, 6),  # Assuming the number of moves increases with more pegs
    (6, 5, 7),  # Assuming the number of moves increases with more slots
    # Add more configurations as needed
])
def test_solve_game_efficiency(pegs, slots, expected_max_moves):
    secret_code = '1234'[:slots]  # Adjust secret code length based on slots
    moves = solve_game(pegs, slots, secret_code)
    assert moves <= expected_max_moves
