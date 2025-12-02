# Input - Prompt for inputs
height = float(input("Enter height (inches): "))
weight = float(input("Enter weight (pounds): "))


# convert to metric
heightMetric = height * 0.0254
weightMetric = weight * 0.453592

# Processing - Calculate the BMI result:
bmi = weight / (height ** 2) * 703
bmiMetric = weightMetric / (heightMetric ** 2)
# Output - Display the result
print('BMIMetric=',bmiMetric)
print("BMI =", bmi)
#formatting the output with the F string
print(f'BMI value for a person height of {height} and weight of {weight} formatted using the F string is: {bmi}')
#using the round function
print("BMI =", round(bmi,2))
print(f'BMI value for a person height of {height} and weight of {weight} formatted using the F string is: {round(bmi,2)}')