#Create four basic mathematical functions: 'add', 
# 'subtract', 'multiply', and 'divide' that take in two numbers and return the result of the operation.

def add(c,d):
    return c + d

def substract(c,d):
    return c - d

def multiply(c,d):
    return c * d

def division(c,d):
    return c/d

#Create a dictionary 'operations' that assigns the functions to their corresponding operation symbols.

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': division
    }


#Create a function 'calculator' that prompts the user to input the first number.

def calculator():
    first_number= float(input("Input first number : "))

#Use a for loop to print the available operation symbols.
#Create a while loop that will continue to run until the user chooses to end the current calculation.
    while True:
        print("Select operation")       
        for operation in operations:
            print(operation)

#Inside the while loop, prompt the user to select an operation symbol.
        operation_input= input("operation selector : ")
        
        operation_input in operations

#Prompt the user to input the second number.
        second_number = float(input("Input second number : "))
#Use the dictionary to retrieve the function that corresponds to the
#  selected operation symbol and store it in a variable 'calculation_function'

        calculator_function = operations[operation_input]
#Perform the calculation by calling the 'calculation_function' on the 
# two input numbers and store the result in a variable 'answer'.

        answer = calculator_function(first_number,second_number)

#Print the equation and the result of the calculation.
        print(f"{first_number} {operation_input} {second_number} = {answer}")


#Ask the user if they would like to continue using the result as the first number for further calculations.
        continue_result = input("Continue with the result ? (yes/no): ") 
        if continue_result =='yes':

#If the user chooses to continue, update the 'num1' variable to the value of 'answer'.
            first_number = answer

#If the user chooses to start a new calculation, set the 'should_continue' variable to 
# false and call the 'calculator' function to start a new calculation.
        else:
            calculator()

calculator()
    

