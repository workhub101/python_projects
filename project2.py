flag=True
with open("project.txt","r") as file:
        contents=file.readlines()
print(contents)
list=contents
def add():
    task1=(input("please enter a task:"))
    list.append(f"{task1}\n")
    print(f"{task1} has been added")
    show()
    with open("project.txt","a") as file:
        file.write(f"{task1}\n")
    

def delete():
    show()
    remove1=int(input("please enter the task that you are removing:"))
    remove1=remove1-1
   
    with open("project.txt","r") as file:
        lines = file.readlines()
    del lines[remove1]
    
    with open("project.txt","w") as file:
        file.writelines(lines)
   
    list.pop(remove1)
    print(list)
    
    show()
def update():
    show()
    update1=int(input("please enter the task number that you want to update:"))
    update1=update1-1
    change1=(input("please enter the task that you are replacing:"))
    list[update1]=change1+"\n"

    with open("project.txt","w") as file:
        file.writelines(list)
   
    show()
def show():
    print(list)
    print("*******************************")
    for i in range(len(list)):
        print(f'{i+1}. {list[i]}')
    print("*******************************")


while(flag):
   
    print("Press 1 : to enter a task to list ")
    print("Press 2 : to delete a task from list")
    print("Press 3 : to update list")
    print("Press 4 : to show list")
    print("Press 5 : to stop code")
    question=(input("choose an option:"))
    if question=="1":
        add()
        continue
    if question=="2":
        delete()
        continue
    if question=="3":
        update()
        continue
    if question=="4":
        show()
        continue
    if question=="5":
        flag=False
        continue
    else:
        print("wrong choice")
