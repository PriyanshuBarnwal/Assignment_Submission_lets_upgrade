# -*- coding: utf-8 -*-
"""Day2_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rEC0jyMPQ1eA8eYRKfhDoH-3kGbgEw1u
"""

lottery = "lets upgrade"
print(lottery)
choosen_character = input("enter a character from the above string as per your choice:- ")

if choosen_character == lottery[0] or choosen_character == lottery[2] or choosen_character == lottery[5] or choosen_character == lottery[7] :
  print("WoooHoo! You won")  
else:
  print("Better Luck Next Time!")