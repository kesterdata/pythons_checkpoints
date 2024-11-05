# 1.Begin by importing the necessary libraries, numpy.
import numpy as np



#2.Use the open() function to open csv file and assign the result to a variable.
with open("Loan_prediction_dataset.csv", "r") as file_object:
    loans = file_object.readlines()

all_loan_amounts = []

for rows in loans[1:]:
    loan_amount = rows.split(",")[8]
    if loan_amount == "":
        continue
    all_loan_amounts.append(int(loan_amount))

print(all_loan_amounts)

loan_array = np.array(all_loan_amounts)

# Use the numpy array to perform some basic statistical analysis on the data, such as finding the mean, median, and standard deviation of the loan amounts.
# 1. Mean
mean = round(np.mean(loan_array), 3)
print(f"The mean is {mean}.")

# 2. Median
median = np.median(loan_array)
print(f"The median is {median}.")

# 3. Standard deviation
standard_deviation = np.std(loan_array)
print(f"The standard deviation is {standard_deviation}.")