def chatbot():
    print("ChatBot: Hello! I'm a simple chatbot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hi there! How can I help you today?")

        elif "how are you" in user_input:
            print("ChatBot: I'm just a bunch of code, but I'm doing great!")

        elif "your name" in user_input:
            print("ChatBot: I'm Rohith, your friendly assistant.")

        elif "help" in user_input:
            print("ChatBot: Sure! You can ask me about weather, greetings, or just chat!")

        elif "weather" in user_input:
            print("ChatBot: I can't fetch real-time data, but I hope it's sunny where you are!")

        else:
            print("ChatBot: I'm not sure how to respond to that. Try asking something else!")

chatbot()
