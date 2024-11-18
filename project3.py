flag=True
students = [
    {
        "id":1,
        "name":"Phill",
        "grade":5,
        "age":10,
        "subject":{"math":80,"science":90,"social_studies":75}
    },
    {
        "id":2,
        "name":"Joey",
        "grade":1,
        "age":6,
        "subject":{"math":60,"science":50,"social_studies":99}    }
]
students
print(students)
def add():
    lenght=len(students)
    name1=(input("what is the name of the student:"))
    grade1=int(input("what grade is this student in:"))
    age1=int(input("how old is this student:"))
    math1=int(input("what your students math grade:"))
    science=int(input("what is this students science grade:"))
    social_studies=int(input("what is the social studies grade of this students:"))
    student = {
        "id":lenght+1,
        "name" : name1,
        "grade": grade1,
        "age": age1,
        "subject":{"math":math1,"science":science,"social_studies":social_studies}
    }
    students.append(student)
def delete():
    remove1=(input("please enter the name you are removing:"))
    for i in range(len(students)):
        
        if remove1 == students[i]["name"]:
            students.pop(i)
            print(f"{remove1} has been deleted from this system")
            
            break
            
        else:
            print("this student is not there")
def update():
    update1=(input("please enter the name of the student that you are updating:"))
    for i in range(len(students)):
        print(students[i]["name"])
        if update1 == students[i]["name"]:
            print("Press 1 : to change name ")
            print("Press 2 : to change grade") 
            print("Press 3 :  to change age")
            print("Press 4 : to change math grade")
            print("Press 5 :  to change social studies grade")
            print("Press 6 : to change science grade")
            change1=int(input("please choose a option:"))
            if change1 == 1 :
                name1=(input("what is the new name of this student:"))
                students[i]["name"]=name1
            if change1 == 2 :
                grade1=int(input("what is the new grade of the student:"))
                students[i]["grade"]=grade1
            if change1 == 3 :
                age1=int(input(" what is the new age of the student:"))
                students[i]["age"]=age1
            if change1 == 4 :
                math1=int(input("what is the new math grade of this student:"))
                students[i]["subject"]["math"]=math1
            if change1 == 5:
                ss1=int(input("what is the new social studies grade of this student:"))
                students[i]["subject"]["social_studies"]=ss1
            if change1 ==6:
                science1=int(input("what is the new science grade of this student:"))
                students[i]["subject"]["science"]=science1
            print(students)


def show():
    for i in range(len(students)):
        print("**********************************************")
        print(f'ID:{students[i]["id"]}')
        print(f'Name:{students[i]["name"]}')
        print(f'Grade:{students[i]["grade"]}')
        print(f'Age:{students[i]["age"]}')
        print(f'Math Grade:{students[i]["subject"]["math"]}')
        print(f'Science Grade:{students[i]["subject"]["science"]}')
        print(f'Social Studies Grade:{students[i]["subject"]["social_studies"]}')
        print("************************************************")

def search():
    for i in range(len(students)):
        search1=(input("what student are you looking for"))
        if search1==students[i]["name"]:
            print(f'ID:{students[i]["id"]}')
            print(f'Name:{students[i]["name"]}')
            print(f'Grade:{students[i]["grade"]}')
            print(f'Age:{students[i]["age"]}')
            print(f'Math Grade:{students[i]["subject"]["math"]}')
            print(f'Science Grade:{students[i]["subject"]["science"]}')
            print(f'Social Studies Grade:{students[i]["subject"]["social_studies"]}')
            break
        else:
            print("student is not present")


        



while(flag):
    print("Press 1 : to add student ")
    print("Press 2 : to update student") 
    print("Press 3 : to delete student")
    print("Press 4 : to show all students")
    print("Press 5 : to stop code")
    print("Press 6 : to search for student")
    question=(input("please choose a option:"))
    if question == "1":
        add()
        print(students)
    if question =="2":
        update()
    if question == "3":
        delete()
    if question == "4":
        show()
    if question == "5":
        flag=False
    if question =="6":
        search()


    
