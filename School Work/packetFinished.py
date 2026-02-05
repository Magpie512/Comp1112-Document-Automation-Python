import random
import time

# Function One - Takes 1 string argument, its job is to build an individual packet for each word in the sentence using a list, each packet is randomly stored in a single list, the final list of lists (packets) stored in a global variable.
def packetBuilder(userInput):
    splitSentence = userInput.split()
    packet = []
    for i in range(len(splitSentence)):
        packet.append(["1.2.3.4", len(splitSentence),i, splitSentence[i], random.randint(0,1)])
    return packet

userInput = input("Enter a sentence: ")
returnedPacket = packetBuilder(userInput) # Calls Function One

print("\nReturned Packet:\n", returnedPacket, "\n")#NEWLINE

# Function Two - Takes one int argument, its job is to build an individual packet for each word in the sentence using a list, each packet is randomly stored in a single list, the final list of lists (packets) stored in a global variable.
def askForPacket(order):
  for i in range(len(returnedPacket)):
    if(returnedPacket[i][2] == order):
      if returnedPacket[i][4] == 1:  # Success
        print("Requested Packet:\n", returnedPacket[i], "\n")
        time.sleep(1)
        return returnedPacket[i]
      else:  # Failed transmission (0), regenerate with new random value
        print("Transmission failed for packet", order, ", retrying...\n")
        time.sleep(1)
        returnedPacket[i][4] = random.randint(0, 1)  # Generate new random value
        return askForPacket(order)  # Recursive call to retry


# Function Three - takes a list argument; its job is to call function 2 and pass an int asking for the packet corresponding to the int argument to be sent. By accessing the global variable 
def identifyMissingPacket():
  lengthOfDataset = len(returnedPacket)
  
  print("Total number of packets in the Dataset: " + str(lengthOfDataset) + "\n")
  
  for order in range(lengthOfDataset):
      print("Requesting packet with order:", order)
      packet = askForPacket(order)
      if packet is None:
          print("Packet with order", order, "is missing.\n")
      else:
          print("Successfully received packet:", packet, "\n")

# Function Four - Takes one int argument, its job is to return the packet corresponing to the int to the caller as a list
def getPacketByOrder(order):
    print("Searching for packet with order:", order)
    for i in range(len(returnedPacket)):
        if returnedPacket[i][2] == order:
            print("Found packet:", returnedPacket[i], "\n")
            return returnedPacket[i]
    print("Packet with order", order, "not found.\n")
    return None

########################################################################################################

# Testing all functions
print("=" * 50)
print("Testing Function Three - identifyMissingPacket()")
print("=" * 50)
identifyMissingPacket()

print("\n" + "=" * 50)
print("Testing Function Four - getPacketByOrder()")
print("=" * 50)
testOrder = 0
result = getPacketByOrder(testOrder)
if result:
    print("Retrieved packet successfully:", result)