from math import factorial

def pascal_triangle(n):
  for i in range(n):
    for j in range(n-i+1):
      print(end=" ")
      
    for j in range(i+1):
      print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()

n = int(input("Enter the number of rows : "))
pascal_triangle(n)
