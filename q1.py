def perfect_number(n):
   sum = 0
   for i in range(1,n): 
      if(n%i == 0):
         sum = sum+i 
   return sum 

n = int(input("Enter number : "))
if(n == perfect_number(n)): 
   print(n, "is a perfect number") 
else: 
   print(n, "is not a perfect number") 

