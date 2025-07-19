import nltk
from nltk.chat.util import Chat, reflections

# Define pattern-response pairs
pairs = [
    # Greetings
    [
        r"hi|hello|hey|greetings",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    # Farewells
    [
        r"bye|goodbye|see you|exit|quit",
        ["Goodbye! Have a great day.", "See you later!", "Bye! Take care."]
    ],
    # Asking chatbot's name
    [
        r"what is your name ?|who are you ?",
        ["I am ChatPy, your simple AI chatbot built with Python and NLTK."]
    ],
    # Asking time
    [
        r"what time is it ?|tell me the time|current time",
        ["I cannot access real-time data in this simple version, but you can check your system clock!"]
    ],
    # Asking about weather
    [
        r"what is the weather ?|how is the weather ?",
        ["I can't check the weather right now, but it's always a good day to learn Python!"]
    ],
    # Asking for help
    [
        r"help|can you help me ?|what can you do ?",
        ["I can chat with you, respond to greetings, and answer simple questions about time, weather, or myself."]
    ],
    # Default fallback
    [
        r"(.*)",
        ["I'm not sure how to respond to that.", 
         "Sorry, I didn't understand. Could you rephrase?", 
         "I'm still learning. Can you try asking differently?"]
    ]
]

# Create and start chatbot
def chatbot():
    print("ChatPy: Hello! I'm ChatPy, your simple AI chatbot.")
    print("Type 'bye' or 'quit' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
