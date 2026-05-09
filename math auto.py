print("hey guys this is my math automation for math problems")
equasion = input("type the math problem here: ")
print(f"you typed this: {equasion}")
import re

# Replace 'x' with '*' for multiplication if present
# This simple regex handles cases like '2x6', '3 x 7', but might need refinement for complex expressions
cleaned_equasion = re.sub(r'(\d+)\s*[xX]\s*(\d+)', r'\1*\2', equasion)

try:
    # Evaluate the cleaned equation
    result = eval(cleaned_equasion)
    print(f"The calculated result for '{equasion}' is: {result}")

    # Now, ask the user for their answer
    user_answer = input("What did you think the answer is? ")

    # Convert user's answer to the same type as the result for comparison (e.g., int, float)
    try:
        if isinstance(result, int):
            user_answer_num = int(user_answer)
        elif isinstance(result, float):
            user_answer_num = float(user_answer)
        else:
            # Fallback for other types, though math results are usually int/float
            user_answer_num = user_answer

        if user_answer_num == result:
            print("That's correct!")
        else:
            print(f"Sorry, that's incorrect. The correct answer was {result}.")
    except ValueError:
        print("Invalid input for your answer. Please enter a number.")

except (SyntaxError, NameError, TypeError) as e:
    print(f"Could not evaluate the equation '{equasion}'. Error: {e}")
    print("Please make sure you entered a valid mathematical expression.")

import random