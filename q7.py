class Student:
  pass 
class Marks:
  pass 
student1 = Student()
marks1 = Marks()
print("Is student1 instance of Student :",isinstance(student1, Student))
print("Is marks1 instance of Student :",isinstance(marks1, Student))
print("Is student1 instance of Marks :",isinstance(student1, Marks))
print("Is marks1 instance of Marks :",isinstance(marks1, Marks)) 
print("Is Student subclass of built-in object class :",issubclass(Student, object))
print("Is Marks subclass of built-in object class :",issubclass(Marks, object)) 
