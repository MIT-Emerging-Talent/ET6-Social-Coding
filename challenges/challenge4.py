# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai

Challenge 4: Data Integrity Verification
Objective:
In this challenge, you'll apply your knowledge of number systems and logical gates to develop a data verification system ensuring transmission integrity. The task involves using logical operations like XOR to compare transmitted and received data.
Scenario:
A company is transmitting data packets over a network and wants to ensure the data is not altered during transmission. To verify data integrity, the company uses a simple checksum.
The data is represented as binary numbers (e.g., "1010101").
The sender creates a checksum by XORing the data with a secret key.
The receiver XORs the received data with the same key and compares the result with the checksum:
If the result is 0, the data is valid.
If the result is not 0, the data is considered altered and invalid.
Task:
Implement a Python program to simulate the sender’s process of generating a checksum using XOR.
Simulate the receiver’s process of verifying the integrity of the received data by comparing the checksum.
You are given:
The data represented as a binary string (e.g., "1010101").
A secret key also represented as a binary string (e.g., "1100110").
Steps to Complete the Task:
Sender:
XOR the data with the key to generate a checksum.
Receiver:
XOR the received data with the same key and compare the result to the checksum. If the result is 0, the data is valid; otherwise, it is invalid.
Key Points :
Input the data and key as binary strings.
Let Python handle the conversion to integers using int(data, 2).
Perform the XOR operation directly on integers.
Optionally convert the result back to binary with bin(), but focus on the XOR operation itself.

"""
#Oleksandr Maksymikhin
#Myint Myat
#Rafaa Ali
#Derek Karungani

data_for_transmission_string = '1010101'
data_for_transmission = int(data_for_transmission_string,2)
security_key = int("1100110",2)
checksum = data_for_transmission ^ security_key
checksum_for_transmission = bin(checksum)



def receiver_verify_data(data_for_transmission_string,checksum_for_transmission):
    data_after_transmission = int(data_for_transmission_string,2)
    receiver_checksum = data_after_transmission ^ security_key
    
    if receiver_checksum == checksum_for_transmission:
        return "Transmission is successful"
    else:
        return "Transmission failed"
      
receiver_verify_data(data_for_transmission_string,checksum_for_transmission)
      