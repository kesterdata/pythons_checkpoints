"""What You're Aiming For

The Interactive Python Quiz Game is a text-based application that presents a series of multiple-choice questions to the user. The game provides instant feedback on each answer and keeps track of the user's score throughout the quiz. This project can be further enhanced with additional features such as random question order, a timer for each question, high score tracking, and a graphical user interface (GUI) using libraries like tkinter.

Note: This checkpoint is optional.


Instructions

Question and Answer Handling:

Display multiple-choice questions to the user.
Capture and validate user inputs.
Provide immediate feedback on the correctness of answers.
Score Tracking:

Keep track of the user's score throughout the quiz.
Display the final score at the end of the quiz.
Randomization:

Randomly shuffle the order of questions for each game session to enhance replayability.
User Interaction:

Simple and intuitive user prompts to navigate through the quiz.
Optional Enhancements:

Implement a timer for each question to add a time-based challenge.
Store and display high scores from previous sessions.
Develop a graphical user interface (GUI) using tkinter for a more interactive experience.
"""



from random import shuffle

questions = [{
    """ 1. What is the name of the cat:
    A. jane
    B. Rainy
    C. Dane
    """ : "A"},

    {"""2. What is pip:
    
    A. class
    B. package
    C. Library

    """ : "B"},


    {"""3. Which is these data structure:
        
    A. class
    B. package
    C. Library

    """:"B"

}]
#shuffle questions
shuffle(questions)

#score tracking

highest_score =0

should_continue = True

def quiz():
    total_score = 0
    global highest_score,should_continue
   
    #Display multiple-choice questions to the user.
    for question_number, question in enumerate (questions, start=1):
        current_question = list(question.keys())[0]
        current_answer = list(question.values())[0]
        print(current_question)


        #Capture user inputs.
        user_response = input("Choose the correct answer : ").capitalize()
        print(user_response)

        #validate  user inputs.
        if user_response == current_answer:
            total_score += 1

        #Provide immediate feedback on the correctness of answers
        else:
            print(f"Your answer was wrong. The current answer is {current_answer} \n")

    highest_score = max(total_score,highest_score)

    #Display total score
    print(f"Your current score is : {total_score} and your highest_score  is : {highest_score}")

    choice = input("Do you want to try again?. Please type yes/no : ").lower()

    if choice == "yes":
        quiz()
    else:
        should_continue = False
        print("Thanks for attempting")

while should_continue:
     quiz()
