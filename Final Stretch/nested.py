import time
phrase = "are"
cracked = False
password = ""

timeStart = time.time()

alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for a in range(len(alphabet)):
    for b in range(len(alphabet)):
        for c in range(len(alphabet)):
            for d in range(len(alphabet)):
                for e in range(len(alphabet)):
                    for f in range(len(alphabet)):
                        for g in range(len(alphabet)):
                            for h in range(len(alphabet)):
                                for i in range(len(alphabet)):
                                    for j in range(len(alphabet)):

                                        now = time.time()
                                        if int(now) - int(timeStart) >= 10:
                                            print("Still running")
                                            timeStart = time.time()  # reset timer

                                        password = (
                                            alphabet[a] + alphabet[b] + alphabet[c] +
                                            alphabet[d] + alphabet[e] + alphabet[f] +
                                            alphabet[g] + alphabet[h] + alphabet[i] +
                                            alphabet[j]
                                        )

                                        if password == phrase:
                                            cracked = True
                                            print("It took " + str(now - timeStart) + " seconds")
                                            print(password)
                                            break
                                        else:
                                            print(password)
