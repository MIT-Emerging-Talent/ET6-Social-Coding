# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

Group name: Salle 8
Group members: Dadi Ishimwe
              Robel Mengsteab
              Safa Saber
              Louis Kervens Hubert
              M Jawid Mohseni
              Mohamed El - nageeb

@author: somai
Challenge 1: Detecting Suspicious Login Attempts
Objective:
The goal of this challenge is to practice Boolean algebra simplification. Students will write a Python program to simplify a
given Boolean expressions using Boolean Algebra’s law, helping them understand how to optimize logical expressions in 
programming.
Scenario:
A cybersecurity team is investigating an authentication system that occasionally flags legitimate login attempts as 
suspicious. The system checks multiple conditions to determine if a login attempt should be blocked.
One of the core checks involves the following rule:
¬(A∧(B∨¬B))
where:
A: The user has provided the correct login credentials.
B: The login attempt is from a trusted device.
The security team suspects that the system might be blocking users incorrectly due to redundant logic checks. Your task is
to simplify the logic to understand what the system is actually doing and determine if the rule is valid or needs 
modification.

Task:
Analyze the given Boolean expression.
Apply Boolean law to simplify it.
Interpret what the final expression means in the context of allowing or blocking a login attempt.

"""
#¬(A∧(B∨¬B))
#¬(A∧(True))
#¬(A∧(1))
#¬(A)

# the authentication system is blocked by incorrect login credentials and not whether the device is trusted or not.
def check_login(A, B):
    """
    A: Correct credentials
    B: Trusted device
    Returns: Whether login should be blocked
    """
    return not A  # Simplified from ¬(A∧(B∨¬B))

# Test cases
print("Credentials correct, trusted device:", check_login(True, True))
print("Credentials correct, untrusted device:", check_login(True, False))
print("Credentials wrong, trusted device:", check_login(False, True))
print("Credentials wrong, untrusted device:", check_login(False, False))
