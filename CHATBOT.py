from datetime import datetime

chat_history = []

def header():
    print("=" * 50)
    print("      SMART SUPPORT CHATBOT")
    print("=" * 50)

def save_message(user, bot):
    chat_history.append((user, bot))

def show_history():
    print("\n----- Chat History -----")
    for user, bot in chat_history:
        print("You :", user)
        print("Bot :", bot)

def greet():
    return "Hello! Welcome to our chatbot."

def courses():
    return """
Available Courses:
1. Python
2. Web Development
3. Data Science
4. Java
5. C Programming
"""

def fees():
    return "Course fees start from Rs. 999."

def contact():
    return """
Email : support@gmail.com
Phone : 9876543210
"""

def address():
    return "Allahabad, Uttar Pradesh"

def certificate():
    return "Certificates are provided after course completion."

def placement():
    return "Placement assistance is available for selected courses."

def internship():
    return "Internship opportunities are available."

def duration():
    return "Course duration varies from 2 to 6 months."

def website():
    return "www.example.com"

def date_info():
    return datetime.now().strftime("%d-%m-%Y")

def time_info():
    return datetime.now().strftime("%H:%M:%S")

header()

while True:

    user = input("\nYou : ").lower()

    if user in ["bye", "quit", "exit"]:
        print("Bot : Goodbye!")
        break

    elif user in ["hi", "hello", "hey"]:
        response = greet()

    elif "course" in user:
        response = courses()

    elif "fee" in user:
        response = fees()

    elif "contact" in user:
        response = contact()

    elif "address" in user:
        response = address()

    elif "certificate" in user:
        response = certificate()

    elif "placement" in user:
        response = placement()

    elif "internship" in user:
        response = internship()

    elif "duration" in user:
        response = duration()

    elif "website" in user:
        response = website()

    elif "date" in user:
        response = date_info()

    elif "time" in user:
        response = time_info()

    elif "history" in user:
        show_history()
        continue

    else:
        response = "Sorry, I didn't understand that."

    print("Bot :", response)
    save_message(user, response)