
import math

class Calculator:
    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Error in division")

    #A method called "add_operation" that takes in two arguments: the operation symbol 
    # and the corresponding function. This method should add the new operation and function to the dictionary.

    def add_operation(self, operational_symbol, function):
        self.operations[operational_symbol] = function


#A method called "calculate" that takes in three arguments: the first number, the operation symbol, and the second number. 
# This method should use the dictionary to determine the appropriate function to perform the calculation.
#  It should also include error handling to check if the operation symbol is valid and if the input values are numbers. 
# If an error is encountered, the method should print an error message and raise an exception.

    def calculate(self, first_number, operational_symbol, second_number=None):
       
        if operational_symbol not in self.operations:
            raise ValueError ("Invalid operational symbol")
        if not isinstance(first_number, int) and not isinstance(second_number,int):
            raise ValueError ("Must be an integer")
        
        if isinstance(first_number, int) and operational_symbol in ["#", "@"] and second_number is None:
            calculation_function = self.operations[operational_symbol]
            answer = calculation_function(first_number)
            return answer
        if isinstance(first_number, int) and operational_symbol in ["^"] :
            calculation_function = self.operations[operational_symbol]
            answer = calculation_function(first_number,second_number)
            return answer
        else:
            calculation_function = self.operations[operational_symbol]
            answer = calculation_function(first_number, second_number)
            return answer
    

#Create separate functions for the advanced mathematical operations (exponentiation, square root, logarithm)
#  and use the "add_operation" method to add them to the calculator's dictionary.

def exponentiation(a, b):
    return a ** b

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        raise ValueError("Error on number inputed")

def logarithm(a):
    if a > 0:
        return math.log(a)
    else:
        raise ValueError("Error on number inputed")
        


calc = Calculator()

calc.add_operation("^", exponentiation)
calc.add_operation("#", square_root)
calc.add_operation("@", logarithm)

#Use the input() function to get input from the user for the numbers and operation symbol.
# Use the math library for advanced mathematical operations
#In the main program, create an instance of the Calculator class, 
# and use a while loop that allows the user to continue performing calculations until they choose to exit.
while True:
    num1 = int(input("Enter first number :"))
    symbol = input("Enter operation symbol : ")
    if symbol in ["@", "#"]:
        result = calc.calculate(num1, symbol)
        print(result)
    else:
        num2 = int(input("Enter second number :"))
        result = calc.calculate(num1, symbol, num2)
        print(result)
    
    exit = input("Do you want to exit this operation? (yes/no): ")
    if exit != "yes":
        break
