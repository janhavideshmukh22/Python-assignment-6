class py_solution:
   def is_valid_parenthese(self, text):
      stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
      for parenthese in text:
        if parenthese in pchar:
          stack.append(parenthese)
        elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
          return False
      return len(stack) == 0

text=input("Enter sequence of brackets : ")
if py_solution().is_valid_parenthese(text) == True:
  print(text, "is valid.")
else:
  print(text, "is not valid.")

