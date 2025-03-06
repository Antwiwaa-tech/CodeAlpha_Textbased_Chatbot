import json
import random
"""Woow"""
"""A textbased chatbot to play games, tell stories, or have a life talk with the system"""

welcome_message = "Hello there, what's your name?"
print(welcome_message)
user_response = input('>> ')

def get_response(prompt):
    """To get user response dynamically"""
    return input(f"{prompt}").lower()

def greeting():
    """Greet the user by name and ask what to do today"""
    print(f'{user_response}, welcome! What would you like to do today?\nGaming, storytelling, or talk?')

greeting()

# Load game outcomes from JSON file
def load_game_data():
    with open("game.json", "r") as file:
        return json.load(file)

# Function to play Rock, Paper, Scissors
def game():
    game_data = load_game_data()  # Load JSON data
    choices = ["rock", "paper", "scissors"]
    
    while True:
        # Get player input
        player_choice = input("\nWelcome to Rock, Paper, Scissors! Type 'quit' to exit.\nChoose rock, paper, or scissors: ").lower()
        
        if player_choice == 'quit':
            print("Exiting game mode...\n")
            break
        elif player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Computer randomly selects a move
        computer_choice = random.choice(choices)

        # Look up the result from JSON file
        result = None
        for round in game_data["rounds"]:
            if round["player"] == player_choice and round["computer"] == computer_choice:
                result = round["result"]
                break

        # Print results based only on the JSON file
        print(f"\nYou chose: {player_choice}")
        print(f"Chatbot chose: {computer_choice}")

        if result:
            print(f"Result: {result.capitalize()}!\n")  # Displays Win, Lose, or Tie
        else:
            print("Something went wrong! No match found in JSON.")

# Load story data
def load_story_data():
    with open("story.json", "r") as file:
        return json.load(file)
    
def story():
    story_data = load_story_data()
    
    # Choose a story randomly
    random_story = random.choice(story_data["stories"])
    print(f"\nStory Time!!!\n{random_story['content']}\n")

while True:
    choice = get_response('>> ')
    if choice == 'gaming':
        game()
    elif choice == 'storytelling':
        story()
    elif choice == 'quit':
        print("Goodbye!")
        break
