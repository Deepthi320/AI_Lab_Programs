def chatbot():
    # Dictionary containing user prompts and bot responses
    conversations = {
        "hello": "Hi there! How can I assist you today?",
        "how are you?": "I'm just a program, but I'm doing great! Thanks for asking.",
        "what is your name?": "I'm your friendly chatbot.",
        "what do you do?": "I can help you with simple tasks and answer questions.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what's the weather like?": "I'm not sure, but you could check a weather app for that!",
        "what is python?": "Python is a versatile programming language used for various applications.",
        "how old are you?": "Age is just a number, and for a bot like me, it's a non-issue.",
        "goodbye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! Let me know if you need anything else."
    }

    # Greeting the user
    print("Chatbot: Hello! I'm a simple chatbot. Ask me something.")

    # Start conversation loop
    while True:
        # Take user input
        user_input = input("You: ").lower()

        # Check if the input matches one of the predefined conversations
        if user_input in conversations:
            print("Chatbot:", conversations[user_input])

            # Break the loop if the user says 'goodbye'
            if user_input == "goodbye":
                break
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else!")

# Start the chatbot conversation
chatbot()
