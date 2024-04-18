import streamlit as st
import random
import itertools

class Mastermind:
    def __init__(self, num_colors, num_slots, secret_code=None):
        self.num_colors = num_colors
        self.num_slots = num_slots
        self.secret_code = secret_code if secret_code else self.generate_random_code()

    def generate_random_code(self):
        return tuple(random.randint(0, self.num_colors - 1) for _ in range(self.num_slots))

    def feedback(self, guess):
        black = sum(1 for i in range(self.num_slots) if guess[i] == self.secret_code[i])
        white = sum(min(guess.count(j), self.secret_code.count(j)) for j in set(guess)) - black
        return black, white

class KnuthSolver:
    def __init__(self, mastermind):
        self.mastermind = mastermind
        self.possible_codes = list(itertools.product(range(mastermind.num_colors), repeat=mastermind.num_slots))

    def reduce_possible_codes(self, guess, response):
        original_count = len(self.possible_codes)
        self.possible_codes = [code for code in self.possible_codes if self.mastermind.feedback(code) == response]
        updated_count = len(self.possible_codes)
        print(f"Reduced possible codes from {original_count} to {updated_count}")

    def next_guess(self):
        if not self.possible_codes:
            return None
        return min(self.possible_codes, key=lambda x: max(sum(1 for code in self.possible_codes if self.mastermind.feedback(x) != self.mastermind.feedback(code)) for response in itertools.product(range(5), repeat=2)))

### Step 3: Streamlit Interface

def main():
    st.title("Mastermind Solver")

    num_colors = st.sidebar.selectbox("Number of Colors", range(3, 16), index=3)
    num_slots = st.sidebar.selectbox("Number of Slots", range(3, 11), index=1)
    game_mode = st.sidebar.radio("Game Mode", ["Autonomous Solver", "Manual Play"])

    mastermind = Mastermind(num_colors, num_slots)

    play_game = st.button("Play Game")

    if play_game:
        if game_mode == "Autonomous Solver":
            if 'solver' not in st.session_state:
                st.session_state.solver = KnuthSolver(mastermind)
                st.session_state.game_active = True
                st.write("Secret Code (hidden): ", mastermind.secret_code)
            if st.session_state.game_active:
                guess = st.session_state.solver.next_guess()
                if guess is None:
                    st.write("No more guesses possible.")
                    st.session_state.game_active = False
                else:
                    response = mastermind.feedback(guess)
                    st.write(f"Guess: {guess} -> Response: {response}")
                    if response == (num_slots, 0):
                        st.write("Code cracked!")
                        st.session_state.game_active = False
                    else:
                        st.session_state.solver.reduce_possible_codes(guess, response)
        elif game_mode == "Manual Play":
            user_guess = st.text_input("Enter your guess (comma-separated numbers):")
            submit_guess = st.button("Submit Guess")  # Button to submit the guess
            if submit_guess:
                if user_guess:
                    guess = tuple(map(int, user_guess.split(',')))
                    response = mastermind.feedback(guess)
                    st.write(f"Your guess: {guess} -> Response: {response}")

if __name__ == "__main__":
    main()
