# Textbased_Chatbot# Chatbot Game and Storytelling System

## Overview
This is a simple text-based chatbot that can play Rock, Paper, Scissors, tell stories, or engage in casual conversation with the user. The chatbot loads data from JSON files to enhance interactivity and provide dynamic responses.

## Features
- **Rock, Paper, Scissors Game**: Play against the chatbot with predefined results.
- **Storytelling Mode**: Listen to random stories from a JSON dataset.
- **Casual Chat Mode**: Have a conversation with the chatbot using predefined responses.
- **User-Friendly Interface**: Simple text input allows easy interaction.
- **JSON-Based Data Handling**: Loads game rules, stories, and responses from JSON files.


## Installation
1. Clone or download the repository.
2. Ensure Python 3.x is installed on your system.
3. Place the JSON files (`game.json`, `story.json`, `response.json`) in the same directory as the script.
4. Run the chatbot using:
   ```sh
   python chatbot.py
   ```

## How to Use
1. When the chatbot starts, enter your name.
2. Choose an action:
   - Type `gaming` to play Rock, Paper, Scissors.
   - Type `storytelling` to listen to a story.
   - Type `talk` to have a conversation with the chatbot.
   - Type `quit` to exit the program.
3. Follow on-screen prompts to interact with the chatbot.

## JSON File Structure
The chatbot relies on three JSON files:
- **`game.json`**: Contains possible results for Rock, Paper, Scissors.
- **`story.json`**: Stores a collection of stories.
- **`response.json`**: Holds predefined inputs and chatbot responses.

## Example JSON Structures
### `game.json`
```json
{
  "rounds": [
    {"player": "rock", "computer": "scissors", "result": "win"},
    {"player": "rock", "computer": "paper", "result": "lose"},
    {"player": "rock", "computer": "rock", "result": "draw"}
  ]
}
```

### `story.json`
```json
{
  "stories": [
    {"content": "Once upon a time..."},
    {"content": "In a faraway land..."}
  ]
}
```

### `response.json`
```json
{
  "greetings": {
    "inputs": ["hello", "hi", "hey"],
    "responses": ["Hello!", "Hi there!", "Hey! How can I assist?"]
  }
}
```

## Error Handling
- The chatbot checks for missing or corrupted JSON files.
- Invalid user inputs are handled with appropriate prompts.
- Users can exit any mode by typing `quit`.

## Future Enhancements
- Improve NLP capabilities for a more interactive chat experience.
- Add more games and stories to the dataset.
- Implement a GUI-based interface.

## Author
Developed by Nana Afua Antwiwaa Conduah.