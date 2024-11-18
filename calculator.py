


Flag=True
while(Flag):
    num1=int(input("Please enter a number"))
    num2=int(input("please enter another number"))
    print("Press 1: to add")
    print("Press 2: to subtract")
    print("Press 3: to multipy")
    print("Press 4: to divide")
    print("Press 5 to end the code ")
            
    operation1=int(input("please choose a operation "))
    if operation1 == 1:
        print(f"{num1}+{num2} = {num1+num2}")
        continue
    if operation1==2:
        print(f"{num1}-{num2} = {num1-num2}")
        continue
    if operation1 ==3:
        print (f"{num1}x{num2}={num1*num2}")
        continue
    if operation1 ==4:
        print(f"{num1}/{num2} = {num1/num2}")
        continue
    if operation1 == 5:
        Flag=False
        continue
    else:
        print("wrong choice")
    
