def get_response(user_input):
    # Predefined rules and responses
    rules = {
        'hello': 'Hello! How can I assist you?',
        'how are you': 'I am just a bot, but thanks for asking!',
        'what is your name': 'I am a chatbot. You can call me ChatBot.',
        'what is the time': 'I am sorry, but I am not equipped to provide real-time information.',
        'bye': 'Goodbye! Have a great day!'
    }

    # Convert the user input to lowercase to handle case-insensitivity
    user_input = user_input.lower()

    # Check for matching patterns and generate responses
    for pattern, response in rules.items():
        if pattern in user_input:
            return response

    # If no predefined rule matches, provide a default response
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("ChatBot: Hello! I am here to help. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()