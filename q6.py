def student_data(student_id, **kwargs):
  print("Student ID :",student_id)
  if 'student_name' in kwargs:
    print("Student Name :",kwargs['student_name'])
  if 'student_class' in kwargs:
    print("Student Class :",kwargs['student_class'])
  print()    

    
student_data(student_id='1')
student_data(student_id='2', student_name='Muskan Choudhary')
student_data(student_id='3', student_name='Janhavi Deshmukh', student_class ='CIVIL')  

