def  get_instructions(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "name" in user_input:
        return "I'm a simple chatbot created to assist you. What's your name?"

    elif "help" in user_input:
        return "I’m here to assist with basic questions. Try asking something simple!"

    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"

    else:
        return "I didn't quite catch that. Could you try saying it another way?"

# main chat starts here looping
print("Chatbot: Hello! Type 'bye' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ai:", get_instructions(user_input))
        break
    else:
        print("ai:", get_instructions(user_input))
