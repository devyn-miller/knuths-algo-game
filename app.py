import streamlit as st
from solver import solve_game
from manual_play import play_manual_game
from solver import generate_random_code

def main():
    st.title("Mastermind Solver")

    game_mode = st.radio("Choose your game mode:", ("Autonomous Solver", "Manual Play"))
    pegs = st.slider("Select number of colored pegs:", 3, 15, 6)
    slots = st.slider("Select number of slots:", 3, 10, 4)
    user_code_input = st.checkbox("Input secret code?")

    if user_code_input:
        secret_code = st.text_input("Enter your secret code:")
    else:
        secret_code = generate_random_code(pegs, slots)

    if st.button("Start Game"):
        if game_mode == "Autonomous Solver":
            solve_game(pegs, slots, secret_code)
        else:
            play_manual_game(pegs, slots, secret_code)

if __name__ == "__main__":
    main()