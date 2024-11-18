Toys=["robot","doll","car","board games","airplanes"]
age1=int(input("what is your age"))
if age1>=6 and age1<=12:
    print("you can be in this toy store")
    robot1=(input("do you like robots"))
    if robot1=="yes":
        
        print("we have great robots")
        toy2=(input("do you want another toy"))
        if toy2=="yes":
            
            doll1=(input("do you want dolls"))
            if doll1=="yes":
                
                print("we have great dolls")
                print("thank you for shopping")
            else:
                car1=(input("do you want a  toy car"))
                if car1=="yes":
                    print("we have great cars thank you for shopping")
                else:
                    toy3=(input("print the toy you want"))
                    if toy3 in Toys:
                        print(f"we have great {toy3}")
                        print("thank you for shopping")
                    else:
                        print("we don't have this product right now")
                

        else:
            
            print("thank you for shopping")

            


    else:
        doll1=(input("do you want doll"))
        if doll1=="yes":
            
            print("we have great dolls")
            toy2=(input("do you want another toy"))
            if toy2=="yes":
                car1=(input("do you want a toy car"))
                if car1=="yes":
                    print("we have great cars")
                    print("thank you for shopping")
                else:
                    toy3=(input("print the toy you would like"))
                    if toy3 in Toys:
                        print(f"we have great {toy3}")
                        print("thank you for shopping")
                    else:
                        print("you would have to wait for this product")
            else:
                print("thank you for shopping")
        else:
            car1=(input("do you want a toy car"))
            if car1=="yes":
                print("we have great cars")
                toy2=(input("do you want another toy"))
                if toy2=="yes":
                    toy3=(input("print the toy you would like"))
                    if toy3 in Toys:
                        print(f"we have great{toy3}")
                        print("thank you for shopping")
                    else:
                        print("this product is not availible")
                        print("thank you for shopping")
                else:
                    print("thank you for shopping")
            else:
                toy3=(input("print the toy you would like"))
                if toy3 in Toys:
                    print(f"we have great {toy3}")
                    print("thank you for shopping")
                else:
                    print("this product is not in store")
                    print("thank  you for stopping by")

            
            
            
    



    
else:
    print("the toys in this toy store are not accessable to you")
