import pytest
from manual_play import play_manual_game
from solver import has_won, can_still_win

# Mocking user inputs and secret code for testing
@pytest.fixture
def mock_inputs(mocker):
    mocker.patch('builtins.input', side_effect=['1234', '5678', '9012', '3456'])
    mocker.patch('manual_play.generate_random_code', return_value='3456')

def test_has_won():
    assert has_won('1234', '1234') == True
    assert has_won('1234', '4321') == False

def test_can_still_win():
    assert can_still_win(3, 5) == True
    assert can_still_win(5, 5) == False

def test_play_manual_game_win(mock_inputs):
    # Assuming the secret code is '3456' and the user guesses it in their last attempt
    assert play_manual_game(6, 4, '3456') == "Congratulations, you've cracked the code!"

def test_play_manual_game_loss(mock_inputs):
    # Assuming the secret code is '3456' but the user fails to guess it within their attempts
    assert play_manual_game(6, 4, '3456') == "Game over. Better luck next time!"