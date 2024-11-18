import turtle
side1=int(input("please enter the number of sides in your shape"))
x=0
y=0
colours=["red","orange","yellow","green","blue","indigo","violet"]
my_turtle=turtle.Turtle()
my_turtle.fillcolor("blue")

angle1=360/side1
print(angle1)
for i in range(7):
    my_turtle.fillcolor(colours[i])
    my_turtle.begin_fill()
    for i in range(side1):
        my_turtle.forward(45)
        my_turtle.left(angle1)
    my_turtle.end_fill()
    x=x+100
    my_turtle.goto(x,y)
   
    
turtle.done()