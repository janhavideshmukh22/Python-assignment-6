def hyphenSep(n):
  l=n.split('-') 
  l.sort() 
  print('-'.join(l)) 

n=input("enter the string: ") 
hyphenSep(n)

