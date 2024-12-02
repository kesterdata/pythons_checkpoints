

questions = {
    """ 1. What is the name of the cat:
    A. jane
    B. Rainy
    C. Dane
""" : "A",

        """2. What is pip:
    
A. class
B. package
C. Library

""" : "B",


"""        3. Which is these data structure:
    
A. class
B. package
C. Library

    """:"B"

}
#score tracking

should_continue = True

def quiz():
        total_score = 0
        highest_score =0
        #Display multiple-choice questions to the user.
        for current_question, current_answer in questions.items():
            print(current_question)

        #Capture user inputs.
            user_response = input("Choose the correct answer : ").capitalize
            print(user_response)

        #validate  user inputs.
        if user_response == current_answer:
            total_score += 1

            #Provide immediate feedback on the correctness of answers
        else:
            print(f"Your answer was wrong. The current answer is {current_answer} \n")
        highest_score = max(total_score,highest_score)

    #Display total score
print(f"Your current score is {total_score} and your highest_score  is{highest_score}")

choice = input("Do you want to try again?. Please type yes/no").lower()
if choice == "yes"