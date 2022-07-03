import string
def isPangram(str):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for char in alphabet:
    if char not in str.lower():
      return False
  return True

text = input("Enter the string : ")
if(isPangram(text) == True):
  print(text,"is a pangram string.")
else:
  print(text,"is not a pangram string.")

