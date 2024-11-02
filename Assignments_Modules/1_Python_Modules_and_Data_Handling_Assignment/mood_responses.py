responses = {
    "happy": "I'm glad to hear that you're feeling happy! Keep smiling!",
    "sad": "I'm sorry to hear that you're feeling sad. Remember, tough times don’t last, but tough people do.",
    "excited": "That's awesome! It sounds like something great is happening. Keep up the excitement!",
    "angry": "It's okay to feel angry sometimes. Take a deep breath, and let's work through it together!",
    "tired": "It sounds like you could use some rest. Don't forget to take breaks and care for yourself!",
    "nervous": "It's natural to feel nervous at times. You got this, just keep going!"
}

def mood_response(mood):
    # Return the corresponding response, or a default response if the mood isn't listed
    return responses.get(mood.lower(), "I'm not sure how to respond to that mood, but I'm here to listen!")

def add_mood(mood, response):
    # Add a new mood and response to the dictionary
    responses[mood.lower()] = response
    return f"Mood '{mood}' added successfully!"