import random
import string

# Questions and Answers
qa_pairs = {
    "courses": [
        "what courses are available",
        "courses offered",
        "available courses",
        "what courses do you offer"
    ],
    "fees": [
        "what is the fee structure",
        "fees details",
        "course fees",
        "how much is the fee"
    ],
    "timings": [
        "what are class timings",
        "class timings",
        "college timings",
        "when are classes conducted"
    ],
    "contact": [
        "contact details",
        "how can i contact college",
        "college contact number",
        "contact information"
    ],
    "admission": [
        "how to apply for admission",
        "admission process",
        "how can i join",
        "admission details"
    ]
}

# Bot responses
responses = {
    "courses": "We offer BCA, B.Sc Computer Science, B.Com, BBA, and MCA courses.",
    "fees": "The fee structure depends on the course. For example, BCA: Rs.45,000/year, BBA: Rs.40,000/year.",
    "timings": "Class timings are from 9:00 AM to 4:00 PM, Monday to Friday.",
    "contact": "You can contact the college at +91 9876543210 or email info@college.edu.",
    "admission": "You can apply for admission online through our college website or visit the admission office.",
    "default": "Sorry, I couldn't understand your question. Please ask about courses, fees, timings, contact, or admission."
}

# Function to clean text
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Function to get response
def get_response(user_input):
    user_input = preprocess(user_input)

    for key, questions in qa_pairs.items():
        for question in questions:
            if question in user_input:
                return responses[key]

    return responses["default"]

# Chatbot starts here
print("=====================================")
print(" Student Query Chatbot ")
print("=====================================")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "bye", "quit"]:
        print("Bot: Thank you! Have a great day.")
        break

    response = get_response(user_input)
    print("Bot:", response)