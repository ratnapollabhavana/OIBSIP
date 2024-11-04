# Function to get valid input for height and weight

def get_valid_input(prompt, min_value, max_value):
    while True:
        value = input(prompt)
        # Check if the input can be converted to a float
        try:
            value = float(value)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            # Provide more specific feedback based on the input
            if value.strip() == "":
                print("Input cannot be empty. Please enter a numeric value.")
            else:
                print(f"'{value}' is not a valid number. Please enter a numeric value.")


# Get user inputs with validation
height = get_valid_input("Enter height in meters (1.0 to 2.5): ", 1.0, 2.5)
weight = get_valid_input("Enter weight in kilograms (10 to 250): ", 10.0, 250.0)

# Define BMI function with accurate thresholds for metric units
def BMI(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 16:
        return "severely underweight", bmi
    elif 16 <= bmi < 17:
        return "moderately underweight", bmi
    elif 17 <= bmi < 18.5:
        return "mildly underweight", bmi
    elif 18.5 <= bmi < 25:
        return "normal weight", bmi
    elif 25 <= bmi < 30:
        return "overweight", bmi
    elif 30 <= bmi < 35:
        return "obese class I (moderate)", bmi
    elif 35 <= bmi < 40:
        return "obese class II (severe)", bmi
    else:
        return "obese class III (very severe)", bmi

# Call the function and print the result
quote, bmi = BMI(height, weight)
print("Your BMI is: {:.2f} and you are: {}".format(bmi, quote))