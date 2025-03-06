import json
import random

"""A text-based chatbot to play games, tell stories, or have a life talk with the system"""

# Load JSON files once at startup
def load_json(file_path):
    """Load JSON data from a given file path."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: {file_path} contains invalid JSON.")
        return None

game_data = load_json("game.json")
story_data = load_json("story.json")
response_data = load_json("response.json")

# Function to get user input
def get_response(prompt):
    """Get user input and return lowercase response."""
    return input(f"{prompt} ").strip().lower()

# Greet the user
# Greet the user and introduce itself
print("\U0001F44B Hello! I am Chatbot, your friendly AI companion. What's your name?")
user_name = get_response(">>")
print(f"\nNice to meet you, {user_name}! I can play games, tell stories, or have a chat.")
print("Just type what you want to do! You can say 'gaming', 'storytelling', or 'talk'. Type 'quit' anytime to exit.")

# Function to play Rock, Paper, Scissors
def game():
    if not game_data:
        print("Game data unavailable. Exiting game mode.")
        return
    try:

        choices = ["rock", "paper", "scissors"]
        
        while True:
            player_choice = get_response("\nRock, Paper, Scissors! (Type 'quit' to exit)\nChoose: rock, paper, or scissors:")

            if player_choice == 'quit':
                print("Exiting game mode...\n")
                return
            if player_choice not in choices:
                print("Invalid choice! Please choose rock, paper, or scissors.")
                continue

            computer_choice = random.choice(choices)
            result = next((r["result"] for r in game_data["rounds"] 
                        if r["player"] == player_choice and r["computer"] == computer_choice), "Unknown")
            
            print(f"\nYou chose: {player_choice}\nChatbot chose: {computer_choice}")
            print(f"Result: {result.capitalize()}!\n" if result != "Unknown" else "Something went wrong! No match found in JSON.")
    
    except Exception as e:
        print(f'Error occured at {e}')

# Function to tell a story
def story():
    if not story_data:
        print("Story data unavailable. Exiting storytelling mode.")
        return

    try:
        random_story = random.choice(story_data["stories"])
        print(f"\nStory Time!!!\n{random_story['content']}\n")
    except (KeyError, IndexError, TypeError):
        print("Error: Story data is missing or corrupted.")

# Function for simple talks
def talk():
    if not response_data:
        print("Sorry, unable to load response data.")
        return
    
    print("\nLet's chat! Type 'quit' to exit.\n")
    
    while True:
        try:
            user_input = input("You: ").strip().lower()

            if user_input == "quit":
                print("Exiting talk mode...\n")
                return

            found_responses = None

            # Check if user input matches any known phrases
            for category in response_data.values():
                if user_input in category["inputs"]:
                    found_responses = category["responses"]
                    break

            # Print response:
            if found_responses:
                print(f"Chatbot: {random.choice(found_responses)}")  # Pick a random response
            else:
                print("Chatbot: Sorry, I can't process that.")

        except Exception as e:
            print(f"Error: {e}")

# Main program loop
try:
    while True:
        action = get_response(">>")
        if action == "gaming":
            game()
        elif action == "storytelling":
            story()
        elif action == "talk":
            talk()
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select: gaming, storytelling, or quit.")
except Exception as e:
    print("Existing program....")            
