import StudentClass as sc

student_id = 1001
name = "Payton"
dob = '11/30/2000'
classification = 'senior'

student1 = sc.Student(student_id, name, dob, classification)

student1.calc_age()
student1.registration()

print(f"Student Name: {name}")
print(f"Student age:  {student1.get_age()}")
print(f"Registration: {student1.get_registration()}")
