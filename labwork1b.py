Students={"id":[], "name":[], "dob":[]}
Courses={"id":[], "name":[]}
Marks=[]

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

def listStudent(n):
  for i in range (0,n):
    print(f"""Student {i+1}:
      ID - {Students["id"][i]}
      Name - {Students["name"][i]}
      DOB - {Students["dob"][i]}
    ---------------------------""")

def listCourses(n):
  for i in range (0,n):
    print(f"""Course {i+1}:
      ID - {Courses["id"][i]}
      Name - {Courses["name"][i]}
    ---------------------------""")

def getMarks(id,name, n):
  print(f"\nEnter the marks of Course {name} - ID {id}:")
  for i in range(0,n):
    Marks.append(input(f"{Students["name"][i]}: "))

def showMarks(id,name,n):

  print(f"Marks of Course {name} - ID {id}:")
  for i in range(0,n):
    print(f"Student {Students["name"][i]} - {Marks[i]}")

def findCrs(id,n):
  for i in range (0,n):
    if (Courses["id"][i]==id):
      return Courses["name"][i]
  print(f"Not Exist Course whose ID is {id}")
  return -1

############### main #################
ns=getS()
getStdInfo(ns)

nc=getC()
getCrsInfo(nc)

#select a course
idc=input("Enter the ID of Course you want to get marks: ")

namecourse=findCrs(idc,nc)
#get id.course (idc) then return name.course
#if cant find id.course, return -1

if (namecourse!=-1):          
  getMarks(idc,namecourse,ns)

print("=============================LIST=========================")
listStudent(ns)
listCourses(nc)

if (namecourse!=-1):
  showMarks(idc,namecourse,ns)