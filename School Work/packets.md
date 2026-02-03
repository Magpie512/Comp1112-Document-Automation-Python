# Notes on packets s and TCP/IP

## Protocol:
* Guidline
* Standard
* Convention
* Contracts
* promise

### TCP (Transmission Control Protocol)
- Guideline, Promise, Contract

Established FORMAL, TWO-WAY, CONNECTION

GUARENTEES ALL DATA IS DELIVERED IN CORRECT SEQUENCE
(Lost Data retransmitted)

Data isnt always transmitted in sequence but it does get resequenced in order on arrival

##### Notes
- set of rules that govern how data is transmitted over a network   
- ensures reliable and ordered delivery of data packets between devices
- establishes a connection between sender and receiver before data transfer
- breaks data into smaller packets for transmission
- manages flow control and error checking to ensure data integrity
- used for applications that require reliable communication, such as web browsing, email, and file transfers

### IP (Internet Protocol)



##### Notes
- responsible for addressing and routing data packets across networks
- assigns unique IP addresses to devices on a network
- determines the best path for data packets to reach their destination
- works in conjunction with TCP to ensure data is delivered to the correct device
- used for routing data across the internet and other networks

Packets:
- small units of data transmitted over a network
- contain both the data being transmitted and control information (such as source and destination addresses)
- broken down into smaller pieces to facilitate efficient transmission and reassembly at the destination
- help optimize network performance and reduce congestion
- used in various networking protocols, including TCP/IP
- Each packet typically consists of a header (with control information) and a payload (the actual data being transmitted)
- Packets are routed independently through the network, allowing for more efficient use of network resources
- At the destination, packets are reassembled into the original data format
- Packets can be lost or corrupted during transmission, so protocols like TCP include mechanisms for error detection and retransmission
- Packets are fundamental to modern networking and enable the efficient transfer of data across the internet and other networks
