# Simple Quiz Card Game

#empty list to store quiz questions
quiz_questions = []

#Function to add a new question
def add_question():
    question = input("Enter the quiz question: ")
    correct_answer = input("Enter the correct answer: ")
    
    #Append a dictionary with the question and answer to the quiz_questions list
    quiz_questions.append({
        "question": question,
        "answer": correct_answer
    })
    print("Question added!\n")

#Function to display available quiz questions with index numbers
def show_available_questions():
    if len(quiz_questions) == 0:
        print("No questions available. Please add some\n")
        return False
    print("\nAvailable Quiz Cards:")
    for i, question_data in enumerate(quiz_questions, start=1):
        print(f"{i}. {question_data['question'][:50]}")  # Show the first 50 characters of the question for preview
    return True

# Function to study a specific quiz card
def study_specific_card():
    if not show_available_questions():
        return
    
    try:
        #Let's choose a specific card by its number
        card_number = int(input("\nEnter the number of the quiz card you want to study: "))
        
        #Validate the input
        if 1 <= card_number <= len(quiz_questions):
            chosen_card = quiz_questions[card_number - 1]  #Access the chosen quiz card (zero-based index)
            print("\n" + chosen_card['question'])  #Display the question
            input("Press flip the question...") #keyboard == enter
            print(f"Answer: {chosen_card['answer']}\n")  # Reveal the answer
        else:
            print("Please choose a quiz card number that is created.\n")
    except ValueError:
        print("Please enter a valid number.\n")

#Main program loop
def main():
    print("Welcome to the Quiz Card Study Tool!")
    while True:
        print("\n1. Add Quiz Question")
        print("2. Study a Specific Card")
        print("3. Exit")
        
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            add_question()  #Add a new question
        elif choice == "2":
            study_specific_card()  #Study a specific quiz card
        elif choice == "3":
            print("Goodbye!")
            break 
        else:
            print("Please choose only from these: 1, 2, or 3.\n")


main()

