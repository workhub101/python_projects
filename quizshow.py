import random
flag=True
score=0
questions=[
    {"question":"What is Shakespheres shortest play","answer":"The Comedy of Errors"},
    {"question":"How many stars are on the USA national flag","answer":"50"},
    {"question":"Which person or company has won the most Oscars","answer":"Walt Disney"},
    {"question":"What is the capital of St. Lucia","answer":"Castries"},
    {"question":"Who won the first football World Cup","answer":"Uruguay"},
    {"question":"Who designed the Eiffel Tower?","answer":"Gustave Eiffel"},
    {"question":"Name the longest river in the UK","answer":"River Serven"},
    {"question":"What is the spiciest chilli in the world","answer":"Carolina reaper" or "carolina reaper"},
    {"question":"How many comformed numbers are in pi","answer":"105 trillion"},
    {"question":"Which playground game used to be an Olympic sport up until 1920","answer":"tug of war"}
]
while(flag):
    print("welcome the the quiz show you will be asked 10 question and for each one you get righr you get a point")
    random.shuffle(questions)
    for i in range(len(questions)):
        answer=input(f'Q){questions[i]["question"]}\n Answer:')
        if answer.lower()==questions[i]["answer"].lower():
            score=score+1
            print("good job, you got the answer right")
            continue
        else:
           print(f'wrong answer\n The right answer was:{questions[i]["answer"]}')
    print(f"good job you got {score}/10")
    score=0 
    question1=input("do you want to try again or leave")
    if question1== "leave":
        flag=False
        print("thank you for playing")
  
    
    
  

   