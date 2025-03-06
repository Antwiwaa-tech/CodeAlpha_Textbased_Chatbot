import json
import random
import openai
import os

"""A text-based chatbot to play games, tell stories, or have a life talk with the system"""

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key")  # Replace with your actual API key

# Load JSON files once at startup
def load_json(file_path):
    """Load JSON data from a given file path."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

game_data = load_json("game.json")
story_data = load_json("story.json")
response_data = load_json("response.json")

# Function to get user input
def get_response(prompt):
    """Get user input and return lowercase response."""
    return input(f"{prompt} ").strip().lower()

# Greet the user
print("Hello there, what's your name?")
user_name = get_response(">>")
print(f"Welcome, {user_name}! What would you like to do today? (gaming, storytelling, or talk?)")

# Function to play Rock, Paper, Scissors
def game():
    if not game_data:
        print("Game data unavailable. Exiting game mode.")
        return

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

# Function to tell a story
def story():
    if not story_data:
        print("Story data unavailable. Exiting storytelling mode.")
        return

    random_story = random.choice(story_data["stories"])
    print(f"\nStory Time!!!\n{random_story['content']}\n")

# Function to have a chat with OpenAI
def talk():
    
    if not response_data:
        print("Sorry, Unable to load response")
        return
    
    print("\nLet's chat! Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You").strip().lower()
        
        if user_input.lower() == "quit":
            print("Exiting talk mode...\n")
            return
        
        found_responses = None
        
    #    Check if user input matches any known phrases"""
         
        for category in response_data.values():
            if user_input in category["inputs"]:
                found_responses = category["responses"]
                break
            
    # Print response:
        if found_responses:
            print(f"Chatbot: {random.choice(found_responses)}") #Pick a random response
            
        else:
            print("Chatbot: Sorry, I can't proccess that")    
       
            
# Main program loop
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