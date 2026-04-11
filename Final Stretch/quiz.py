import pyinputplus as pyip

def run_quiz():
    score = 0
    
    print("--- Welcome to the PyInputPlus Quiz! ---")

    # Question 1: Multiple Choice
    q1_prompt = "\n1. Which keyword is used to handle exceptions in Python?\n"
    response1 = pyip.inputMenu(['try', 'catch', 'throw', 'except'], 
                                prompt=q1_prompt, 
                                numbered=True)
    
    if response1 == 'except':
        print("Correct!")
        score += 1
    else:
        print("Incorrect. 'except' is the Python way.")

    # Question 2: Timed Numeric Question
    print("\n2. Quick! What is 12 x 12?")
    try:
        response2 = pyip.inputInt(prompt="Answer: ", 
                                  limit=2, 
                                  timeout=5, 
                                  default=-1)
        
        if response2 == 144:
            print("Fast and accurate! +1 point.")
            score += 1
        elif response2 == -1:
            print("Out of time or attempts!")
        else:
            print("Not quite.")
            
    except pyip.RetryLimitException:
        print("Too many wrong guesses.")

    print(f"\nFinal Score: {score}/2")

if __name__ == "__main__":
    run_quiz()