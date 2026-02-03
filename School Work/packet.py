"""
Mars Briggs
200561234
02-03-26
Packet Nonsense
"""
import random
import time

# Function One - Takes 1 string argument, its job is to build an individual packet for each word in the sentence using a list, each packet is randomly stored in a single list, the final list of lists ( packets) stored in a global variable.
def buildPacket(sentence):
    splitSentence = sentence.split()
    packet = []
    for i in range(len(splitSentence)):
        packet.append(["1.2.3.4", len(splitSentence),i, splitSentence[i], random.randint(0,1)])
    return packet

userSentence = input("Enter a sentence: ")
returnedPacket = buildPacket(userSentence) # Calls Function One

print(returnedPacket)

print()#NEWLINE
print("Order Below \n")

# Function Two - Takes one int argument, its job is to build an individual packet for each word in the sentence using a list, each packet is randomly stored in a single list, the final list of lists ( packets) stored in a global variable.

""" TEST
returnedPacket = [['1234',4,1,'hello', 1],['1234',4,2,'hello', 1]]
"""
order = 1

def askForPacket(order):
  for i in range(len(returnedPacket)):
    if(returnedPacket[i][2] == order):
      print(returnedPacket[i])
      time.sleep(1)
      return returnedPacket[i]
      
askForPacket(order)

print()#NEWLINE
print("List Below \n")


# Function Three - takes a list argument; its job is to call function 2 and pass an int asking for the packet corresponding to the int argument to be sent. By accessing the global variable 
def AskForMissing():
  lengthOfDataset = 0
  
  #Finds the length of the dataset
  for i in range (len(returnedPacket)):
    lengthOfDataset = lengthOfDataset + 1
    
  #Remove one to simulate asking for missing
  newDataset = returnedPacket.remove(order) #"not in list error"

  print("Total number of packets in the Dataset: " + str(lengthOfDataset) + "\n")
  print("New Address(Missing One): " + newDataset)
  
AskForMissing()


print()#NEWLINE

# Function Four - Takes one int argument, its job is to return the packet corresponing to the int to the caller as a list
def function4(i):
  return buildPacket(userSentence)[i][3]