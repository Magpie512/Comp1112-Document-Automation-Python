import time

alphabet = ['a', 'b', 'c', 'd']
password = 'dacdab'

timeStart = time.time()

def bruteForce():
    now = time.time()
    # We use 6 loops for the 6-character password 'abcdab'
    for i in range(4):# Guesses the first character
        for j in range(4): # Guesses the second character
            for k in range(4): # Guesses the third character
                for l in range(4): # Guesses the fourth character
                    for m in range(4): # Guesses the fifth character
                        for n in range(4): # Guesses the sixth character
                            # Construct the guess
                            guess = alphabet[i] + alphabet[j] + alphabet[k] + \
                                    alphabet[l] + alphabet[m] + alphabet[n]
                            
                            # Print every attempt as requested
                            if now - timeStart >=30:
                                print("Still running")
                            print("Trying: " + guess)
                            
                            if guess == password:
                                print("Match Found: " + guess)
                                return # This exits the entire function immediately

bruteForce()

finishTime = str(time.time() - timeStart)
# trim and round to 2 decimal places
finishTime = round(float(finishTime), 2)

print("Script finished in " + str(finishTime) + "seconds.")
