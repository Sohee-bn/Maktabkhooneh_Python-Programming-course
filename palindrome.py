# -*- coding: utf-8 -*-
"""palindrome

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-VbPDPSVXB8c5R_YUbueu6oGAHeZXkYt
"""

def isPalindrome(str):
  for i in range(0, int(len(str)/2)):
    if str[i] != str[len(str)-i-1]:
      return False
  return True
 

s = input()
s=s.lower()
ans = isPalindrome(s)
 
if (ans):
    print("palindrome")
else:
    print("not palindrome")