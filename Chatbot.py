def chatbot():
    print("Welcome to ChatBot,Let's Chat! and type 'end' for exit")

    while True:
        response=input("You:").lower().strip()

        if response=="end":
            print("Bot: Chat ended, Thanks for chatting with me👋")
            break

        if response=="hi" or response=="hello":
            print ("Bot: Hello!☺️  I'm there, How can I help you today?")
        elif response=="your name":
            print ("Bot: I'm a Rule-Based ChatBot!, Designed to assist you.")
        elif response=="how are you":
            print ("Bot: I'm Good👍,thanks for asking and What about you?")
        elif response=="bye":
            print ("Bot: Bye for now👋,Have a nice day!✨")
        else:
            print ("Oops!, I couldn't Understand your message.")

if __name__=="__main__":
    chatbot()

        
         
        