# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
# from PyQt5.QtCore import Qt

# import itertools

# class MastermindSolver:
#     def __init__(self):
#         self.possible_codes = list(itertools.product(range(6), repeat=4))
#         self.guesses = []

#     def feedback(self, guess, secret):
#         black = sum(g == s for g, s in zip(guess, secret))
#         white = sum(min(guess.count(n), secret.count(n)) for n in set(guess)) - black
#         return black, white

#     def reduce_possible_codes(self, guess, response):
#         self.possible_codes = [code for code in self.possible_codes if self.feedback(guess, code) == response]

#     def next_guess(self):
#         if not self.guesses:
#             return (0, 0, 1, 1)  # Knuth's initial guess
#         scores = []
#         for guess in set(self.possible_codes):
#             score = max(sum(1 for code in self.possible_codes if self.feedback(guess, code) != response)
#                         for response in itertools.product(range(5), repeat=2))
#             scores.append((score, guess))
#         return min(scores)[1]

#     def solve(self, secret, step_by_step=False):
#         while True:
#             guess = self.next_guess()
#             self.guesses.append(guess)
#             response = self.feedback(guess, secret)
#             if response == (4, 0):
#                 if step_by_step:
#                     for i, guess in enumerate(self.guesses, 1):
#                         print(f"Guess {i}: {guess}")
#                 else:
#                     print(f"Solved in {len(self.guesses)} guesses.")
#                 break
#             self.reduce_possible_codes(guess, response)

# if __name__ == "__main__":
#     solver = MastermindSolver()
#     secret_code = (1, 2, 3, 4)  # Example secret code
#     step_by_step = input("Show step-by-step solution? (yes/no): ").lower() == "yes"
#     solver.solve(secret_code, step_by_step)

# class MastermindApp(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.init_ui()

#     def init_ui(self):
#         # Set up the layout and widgets

#         self.show()


# # Add a label and input field for the guess
# self.guess_label = QLabel("Guess:")
# self.guess_input = QLineEdit()

# # Add a button to submit the guess
# self.submit_button = QPushButton("Submit")

# # Add a label to display the feedback
# self.feedback_label = QLabel("")

# # Add a label to display the number of attempts
# self.attempts_label = QLabel("Attempts: 0")

# # Set up the layout
# layout = QVBoxLayout()
# layout.addWidget(self.guess_label)
# layout.addWidget(self.guess_input)
# layout.addWidget(self.submit_button)
# layout.addWidget(self.feedback_label)
# layout.addWidget(self.attempts_label)

# self.setLayout(layout)

# self.submit_button.clicked.connect(self.handle_guess)

# def handle_guess(self):
#     # Get the user's guess
#     guess = self.guess_input.text()

#     # Validate the guess
#     if not guess.isdigit() or len(guess) != 4:
#         self.feedback_label.setText("Invalid guess. Please enter a 4-digit number.")
#         return

#     # Convert the guess to a list of integers
#     guess_list = [int(digit) for digit in guess]

#     # Implement the Mastermind game logic here

#     # Update the feedback and number of attempts
#     self.feedback_label.setText("Feedback: " + feedback)
#     self.attempts_label.setText("Attempts: " + str(attempts))

# if __name__ == "__main__":
#     app = QApplication([])
#     ex = MastermindApp()
#     sys.exit(app.exec_())


