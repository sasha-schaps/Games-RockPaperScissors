<!--Game for Simple Rock Paper Scissors-->

import random

def get_user_choice():
  """Gets valid input from the user."""
  choices = ['rock', 'paper', 'scissors']
  user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
  while user_choice not in choices:   

    user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()   

  return user_choice

def get_computer_choice(difficulty):
  """Generates the computer's choice based on difficulty."""
  choices = ['rock', 'paper', 'scissors']
  if difficulty == "easy":
    return random.choice(choices)  # Completely random
  elif difficulty == "medium":
    # Add some logic here later (e.g., slight bias)
    return random.choice(choices) 
  elif difficulty == "hard":
    # Add more advanced logic here later (e.g., pattern analysis)
    return random.choice(choices)
  else:
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
  """Determines the winner of the round."""
  if user_choice == computer_choice:
    return "It's a tie!"
  elif (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
    return "You win!"
  else:
    return "Computer wins!"

def play_game():
  """Main   
 game loop."""
  user_score = 0
  computer_score = 0

  while True:
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    user_choice = get_user_choice()
    computer_choice = get_computer_choice(difficulty)

    print(f"Computer chose {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
      user_score += 1
    elif result == "Computer wins!":
      computer_score += 1

    print(f"Score   
 - You: {user_score}, Computer: {computer_score}")

    play_again = input("Play   
 again? (y/n): ").lower()
    if play_again != 'y':
      break

if __name__ == "__main__":
  play_game()
