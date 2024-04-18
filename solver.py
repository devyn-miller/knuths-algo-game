import random
from itertools import product
import streamlit as st

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

def solve_game(pegs, slots, secret_code, feedback_func):
    """
    Solve the game using provided feedback function instead of input().
    feedback_func is a function that takes the current guess and returns black_pegs, white_pegs.
    """
    colors = pegs
    possible_codes = generate_possible_codes(slots, colors)
    attempts = 0
    while len(possible_codes) > 1:
        attempts += 1
        guess = possible_codes[0]
        black_pegs, white_pegs = feedback_func(guess)
        feedback = (black_pegs, white_pegs)
        possible_codes = [code for code in possible_codes if calculate_feedback(code, guess) == feedback]
    return possible_codes[0], attempts

# Note: play_manual_game function will be adapted in a similar way if needed.


def feedback_func(guess):
    """
    Collect feedback for a given guess using Streamlit sliders.
    """
    st.write(f"Guess: {guess}")
    black_pegs = st.slider("Black pegs (correct color, correct position):", 0, len(guess), 0, key=f"black_{guess}")
    white_pegs = st.slider("White pegs (correct color, wrong position):", 0, len(guess) - black_pegs, 0, key=f"white_{guess}")
    return black_pegs, white_pegs

def pin_color_to_rgb(pin):
    color_map = {
        'Red': [255, 0, 0],
        'Green': [0, 255, 0],
        'Blue': [0, 0, 255],
        'Yellow': [255, 255, 0],
        'Black': [0, 0, 0],
        'White': [255, 255, 255],
        'Orange': [255, 165, 0],
        'Purple': [128, 0, 128],
        'Pink': [255, 192, 203],
        'Brown': [165, 42, 42],
        'Cyan': [0, 255, 255],
        'Magenta': [255, 0, 255],
        'Lime': [0, 255, 0],
        'Gray': [128, 128, 128],
        'Navy': [0, 0, 128],
    }
    return color_map.get(pin, [0, 0, 0])  # Default to black if color not found

def visualize_game(secret_code, guesses):
    import pydeck as pdk
    # Convert secret_code and guesses to visual representation
    # This is a placeholder for the actual visualization logic
    # You will need to create layers for pydeck here

    # Example of creating a layer for pydeck
    # This should be adapted to your game's visualization needs
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=[{'position': [i, 0], 'color': pin_color_to_rgb(pin)} for i, pin in enumerate(secret_code)],
        get_position='[longitude, latitude]',
        get_color='[color[0], color[1], color[2], 150]',
        get_radius=100,
    )
    st.pydeck_chart(pdk.Deck(layers=[layer]))

def main():
    st.title("Mastermind Solver")

    game_mode = st.radio("Choose your game mode:", ("Autonomous Solver", "Manual Play"))
    pegs = st.slider("Select number of colored pegs:", 3, 15, 6)
    slots = st.slider("Select number of slots:", 3, 10, 4)
    user_code_input = st.checkbox("Input secret code?")

    if user_code_input:
        secret_code = []
        for i in range(slots):
            color = st.selectbox(f"Select color for pin {i+1}:", options=['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White', 'Orange', 'Purple', 'Pink', 'Brown', 'Cyan', 'Magenta', 'Lime', 'Gray', 'Navy'], index=0, key=f"pin_{i}")
            secret_code.append(color)
        secret_code = ''.join(secret_code)

    if st.button("Start Game"):
        if game_mode == "Autonomous Solver":
            solution, attempts = solve_game(pegs, slots, secret_code, feedback_func)
            st.write(f"Solution found in {attempts} attempts: {solution}")
            visualize_game(secret_code, [solution])
        else:
            st.write("Manual play mode is not yet implemented for Streamlit.")

if __name__ == "__main__":
    main()
