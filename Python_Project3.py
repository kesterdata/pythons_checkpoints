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
