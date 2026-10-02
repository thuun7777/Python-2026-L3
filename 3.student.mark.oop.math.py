"""have not worked with CURSES module yet"""
import math
import numpy as np

Students=[]
Students.append({"id": 2535, "name": "Sleepy Lady", "dob": "12/12/2007", "GPA": 0})
Students.append({"id": 2536, "name": "Le Garcon", "dob": "14/11/2007", "GPA": 0})
Students.append({"id": 2338, "name": "Skibydy Ye", "dob": "10/04/2007", "GPA": 0})
Students.append({"id": 2542, "name": "Happy Cat", "dob": "11/08/2007", "GPA": 0})

Courses=[]
Courses.append({"id":1001, "name":"Physique", "credits": 4})
Courses.append({"id":1004, "name":"Mathématiques", "credits": 5})
Courses.append({"id":1007, "name":"Informatique", "credits": 3})
          
Marks=[]
Marks.append([8.12345, 5.1, 7.5, 9.12345])
Marks.append([9.006, 6.2345, 8.125, 9.8765])
Marks.append([8.88055, 7.1155, 7.625, 9.35005])

"""
def getS():
  n=int(input("Number of students: "))
  return n

def getC():
  n=int(input("Number of courses: "))
  return n

def getStdInfo(n):
  for i in range (0,n):
    print("Student ",i+1)
    Students["id"].append(input("ID "))
    Students["name"].append(input("Name "))
    Students["dob"].append(input("DOB "))

def getCrsInfo(n):
  for i in range(0,n):
    print("Course ",i+1)
    Courses["id"].append(input("ID "))
    Courses["name"].append(input("Name "))
"""

def listStudent(n):
  for i in range (0,n):
    print(f"""Student {i+1}:
      ID - {Students[i]["id"]}
      Name - {Students[i]["name"]}
      DOB - {Students[i]["dob"]}""")
    if (Students[i]["GPA"]!=0):
      print(f"      GPA - {Students[i]["GPA"]}")
    print("    ---------------------------")

def listCourses(n):
  for i in range (0,n):
    print(f"""Course {i+1}:
      ID - {Courses[i]["id"]}
      Name - {Courses[i]["name"]}
      Credits - {Courses[i]["credits"]}
    ---------------------------""")
#  print("You must now enter the marks for each student for each course.")
#  print("=======================ENTER==MARKS=======================")

def getMarks(n1, n2):
  for i in range (0,n2):
    print(f"For Course {Courses[i]["id"]} - {Courses[i]["name"]}:")
    temp=[]
    for j in range (0,n1):
      mrk=float(input(f"Student {Students[j]['name']}: "))
      temp.append(mrk)
    Marks.append(temp)

def roundMarks(n1, n2):
  for i in range (0,n2):
    for j in range(0,n1):
        #Where I USE THE MATH LIBRARY
        Marks[i][j]=math.floor(Marks[i][j]*10)/10

def showMarks(n1, n2):
  for i in range (0,n2):
    print(f"Marks for Course {Courses[i]['name']} - ID {Courses[i]['id']}:")
    for j in range (0,n1):
      print(f"Student {Students[j]['name']}: {Marks[i][j]}")
    print("---------------------------")

#a function to calculate GPA for a given student whose info - id
def getGPA(id,nc):
  mrk=[]
  cre=[]
  for i in range (0,nc):
    mrk.append(Marks[i][id])
    cre.append(Courses[i]["credits"])
  #Where I USE THE NUMPY LIBRARY
  mrk = np.array(mrk)
  cre = np.array(cre)
  gpa = np.sum(cre * mrk) / np.sum(cre)
  gpa = math.floor(gpa *10)/10
  return gpa


#-------------------------------------main---------------------
print('The student data were initially collected. (ID, Name, DOB, Marks)')
print('The course data were initially collected. (ID, Name, Credits)')
ns=4
nc=3
#getStdInfo(ns)
#getCrsInfo(ns)

print("==========================LISTING========================")
listStudent(ns)
listCourses(nc)
#getMarks(ns, nc)

roundMarks(ns,nc)
showMarks(ns,nc)
print("======================LISTING  COMPLETED==================")

print("GPA of",ns,"students:")
for i in range (0,ns):
  gpa=getGPA(i,nc)
  Students[i]["GPA"]=gpa
  print(f"{i+1}. Student {Students[i]['name']} has GPA: {gpa}")
print("---------------------------")

print("After sorting student list by GPA descending:")
Students.sort(key=lambda s: s["GPA"], reverse=True)
listStudent(ns)