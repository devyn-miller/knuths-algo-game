from utils import has_won, calculate_max_unlucky_moves, can_still_win

def play_manual_game(pegs, slots, secret_code):
    max_unlucky_moves = calculate_max_unlucky_moves(pegs, slots)
    print(f"The maximum number of moves if you're as unlucky as possible is: {max_unlucky_moves}")
    
    user_attempts = int(input("Enter the number of attempts you want to use to solve the game: "))
    moves_taken = 0
    
    while moves_taken < user_attempts:
        user_guess = input("Enter your guess: ")
        moves_taken += 1
        
        # Provide feedback on the guess
        
        if can_still_win(moves_taken, user_attempts):
            print("You can still guarantee a win with optimal play.")
        else:
            print("You can no longer guarantee a win with the remaining moves.")
        
        if has_won(secret_code, user_guess):
            print("Congratulations, you've cracked the code!")
            break
    else:
        print("Game over. Better luck next time!")