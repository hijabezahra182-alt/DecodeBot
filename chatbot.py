
import re
from data.responses import RESPONSES


# Alternative ways users may ask questions
ALIASES = {

    "what is ai": [
        "explain ai",
        "define ai",
        "tell me about ai",
        "meaning of ai",
        "explain artificial intelligence",
        "define artificial intelligence"
    ],

    "how does ai work": [
        "how ai works",
        "working of ai",
        "how artificial intelligence works"
    ],

    "types of ai": [
        "what are the types of ai",
        "different types of ai",
        "categories of artificial intelligence"
    ],

    "what is machine learning": [
        "explain machine learning",
        "define machine learning",
        "meaning of machine learning",
        "what is ml",
        "explain ml"
    ],

    "what is deep learning": [
        "explain deep learning",
        "meaning of deep learning"
    ],

    "what is generative ai": [
        "explain generative ai",
        "what does generative ai mean"
    ],

    "difference between ai and ml": [
        "ai vs ml",
        "difference of ai and ml",
        "compare ai and machine learning",
        "how is ai different from ml"
    ],

    "what is python": [
        "explain python",
        "define python",
        "what does python mean",
        "tell me about python"
    ],

    "why use python": [
        "why do we use python",
        "benefits of python",
        "advantages of python",
        "importance of python",
        "what makes python popular"
    ],

    "applications of python": [
        "uses of python",
        "where is python used",
        "what can we do with python",
        "what is python used for"
    ],

    "what is a variable": [
        "explain variable",
        "what are variables",
        "meaning of variable"
    ],

    "what is a loop": [
        "explain loop",
        "what are loops",
        "types of loops",
        "why use loops"
    ],

    "what is a function": [
        "explain function",
        "what are functions",
        "why use functions",
        "purpose of functions"
    ],

    "what is a list": [
        "explain list",
        "what are lists",
        "python lists"
    ],

    "what is a dictionary": [
        "explain dictionary",
        "what are dictionaries",
        "python dictionary"
    ],

    "what is programming": [
        "explain programming",
        "meaning of programming",
        "what does programming mean"
    ],

    "what is an algorithm": [
        "explain algorithm",
        "what are algorithms",
        "meaning of algorithm"
    ],

    "what is data science": [
        "explain data science",
        "meaning of data science"
    ],

    "what is an api": [
        "explain api",
        "what does api mean",
        "meaning of api",
        "application programming interface"
    ],

    "what is cloud computing": [
        "explain cloud computing",
        "meaning of cloud computing"
    ]
}


def normalize_text(text):
    """Normalize user input."""

    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text


def get_response(user_input):
    """Generate a rule-based response."""

    original_input = user_input.strip()
    user_input = normalize_text(user_input)

    if not user_input:
        return "Please enter a message!"

    # Greetings
    greetings = [
        "hi", "hy", "hii", "hiii", "hello",
        "hey", "heyy", "good morning",
        "good afternoon", "good evening"
    ]

    if user_input in greetings:
        return "Hello! Welcome to DecodeBot. How can I help you today?"

    # Exit commands
    if user_input in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye! Thank you for chatting with DecodeBot. Have a wonderful day!"

    # Help
    if user_input in ["help", "commands", "what can i ask"]:
        return (
            "Welcome to DecodeBot! Here are the topics I can help with:\n\n"
            "• Artificial Intelligence\n"
            "• Machine Learning\n"
            "• Deep Learning\n"
            "• Python Programming\n"
            "• Programming Concepts\n"
            "• Data Science\n"
            "• APIs and Cloud Computing\n"
            "• Cybersecurity and Technology\n"
            "• Jokes and Fun Facts\n\n"
            "Ask me a question in your own words!"
        )

    # Thank you
    if user_input in ["thanks", "thank you", "thx", "thankyou"]:
        return "You're very welcome! Happy to help."

    # How are you?
    if user_input in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking. What would you like to explore?"

    # Search all predefined questions and aliases
    best_match = None
    best_score = 0

    for category, questions in RESPONSES.items():

        for question, answer in questions.items():

            possible_questions = [question]

            possible_questions.extend(ALIASES.get(question, []))

            for possible_question in possible_questions:

                normalized_question = normalize_text(possible_question)

                # Exact match
                if user_input == normalized_question:
                    return answer

                # Phrase contained in user's question
                if normalized_question in user_input:
                    score = len(normalized_question.split())

                    if score > best_score:
                        best_score = score
                        best_match = answer

    if best_match:
        return best_match

    # Unknown question
    return (
        "That's an interesting question! However, I don't have a "
        "predefined answer for it yet.\n\n"
        "I can currently help you with Artificial Intelligence, "
        "Python Programming, Machine Learning and Technology.\n\n"
        "Try asking a question about one of these topics!"
    )
