# Dominic Baillie
# 200645091
# 4/04/2026
# Working with pdf files

#abcdab - Password

import PyPDF2, time

alphabet = ['a', 'b', 'c', 'd']
timeThirty = time.time()

def deCrypt():
    password = ''
    # Loop through every possible letter
    global alphabet, timeThirty
    timeStart = time.time()
    for i in range(0, 4):
        if(int(time.time())-int(timeThirty) >= 30):
            print('Still running')
            timeThirty = time.time()
        for j in range(0, 4):
            for k in range(0, 4):
                for m in range(0 ,4):
                    for n in range(0, 4):
                        for o in range(0, 4):
                            for j in range(0, 4):
                                if(not pdfReader.is_encrypted):
                                    print('END')
                                    break
                                else:
                                    password = str(alphabet[i])+str(alphabet[j])+str(alphabet[k])+str(alphabet[m])+ str(alphabet[n])+ str(alphabet[o])+ str(alphabet[j])
                                    pdfReader.decrypt(password)
                                    # print(password)

def deCrypt2():
    password = ''
    # Loop through every possible letter
    global alphabet, timeThirty
    timeStart = time.time()
    for i in range(0, 4):
        if(int(time.time())-int(timeThirty) >= 30):
            print('Still running')
            timeThirty = time.time()
        for j in range(0, 4):
            for k in range(0, 4):
                for m in range(0 ,4):
                    for n in range(0, 4):
                        for o in range(0, 4):
                            for j in range(0, 4):
                                if(not pdfReader.is_encrypted):
                                    print('END')
                                    break
                                else:
                                    password = str(alphabet[i])+str(alphabet[j])+str(alphabet[k])+str(alphabet[m])+ str(alphabet[n])+ str(alphabet[o])+ str(alphabet[j])
                                    pdfReader.decrypt(password)
                                    # print(password)

def deCrypt3():
    global alphabet, timeThirty
    timeStart = time.time()
    for i in range(0, 4):
        if(int(time.time())-int(timeThirty) >= 30):
            print('Still running')
            timeThirty = time.time()
        for j in range(0, 4):
            for k in range(0, 4):
                for m in range(0 ,4):
                    for n in range(0, 4):
                        for o in range(0, 4):
                            for j in range(0, 4):
                                for k in range(0,4):
                                    if(not pdfReader.is_encrypted):
                                        print('END')
                                        break
                                    else:
                                        password = str(alphabet[i])+str(alphabet[j])+str(alphabet[k])+str(alphabet[m])+ str(alphabet[n])+ str(alphabet[o])+ str(alphabet[j])+ str(alphabet[k])
                                        pdfReader.decrypt(password)

def deCrypt4():                                        # print(password)
    global alphabet, timeThirty
    timeStart = time.time()
    for i in range(0, 4):
        if(int(time.time())-int(timeThirty) >= 30):
            print('Still running')
            timeThirty = time.time()
        for j in range(0, 4):
            for k in range(0, 4):
                for m in range(0 ,4):
                    for n in range(0, 4):
                        for o in range(0, 4):
                            for j in range(0, 4):
                                for k in range(0,4):
                                    for l in range(0,4):
                                        if(not pdfReader.is_encrypted):
                                            print('END')
                                            break
                                        else:
                                            password = str(alphabet[i])+str(alphabet[j])+str(alphabet[k])+str(alphabet[m])+ str(alphabet[n])+ str(alphabet[o])+ str(alphabet[j])+ str(alphabet[k])+ str(alphabet[l])
                                            pdfReader.decrypt(password)
                                            # print(password)
                                            
def deCrypt5():
    password = ''
    # Loop through every possible letter
    global alphabet, timeThirty
    timeStart = time.time()
    for i in range(0, 4):
        if(int(time.time())-int(timeThirty) >= 30):
            print('Still running')
            timeThirty = time.time()
        for j in range(0, 4):
            for k in range(0, 4):
                for m in range(0 ,4):
                    for n in range(0, 4):
                        for o in range(0, 4):
                            if(not pdfReader.is_encrypted):
                                print('END')
                                break
                            else:
                                password = str(alphabet[i])+str(alphabet[j])+str(alphabet[k])+str(alphabet[m])+ str(alphabet[n])+ str(alphabet[o])
                                pdfReader.decrypt(password)
                                # print(password)
    
    stop = time.time()
    print('It took '+ str(stop-timeStart))

    
    deCrypt2()
    stop = time.time()
    print('It took '+ str(stop-timeStart))


    deCrypt3()
    stop = time.time()
    print('It took '+ str(stop-timeStart))


    deCrypt4()
    stop = time.time()
    print('It took '+ str(stop-timeStart))


    deCrypt5()
    stop = time.time()
    print('It took '+ str(stop-timeStart))
    
    
    
# Print the pdf
pdfFile = open('School Work/Lesson 12/ThePDF.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)
# pdfReader.decrypt('abcdab')
if(pdfReader.is_encrypted):
    deCrypt()
pdfPage = pdfReader.pages[0]
print(pdfPage.extract_text())


