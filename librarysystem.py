class LibrarySystem:
    def __init__(self,name,) -> None:
        self.name=name
        
        self.books=[]
            
   



    def add(self):
        name1=(input("what is the name of the book:"))
        author1=(input("what is the author of this book:"))
        book ={
            "name":name1,
            "author":author1,
            "borrow":False
        }
        self.books.append(book)
    def borrow(self):
        borrow1=(input("what is the title of the book you are borrowing: ")) 
        is_book_found=False   
        for i in range(len(self.books)):
            if borrow1.lower()==self.books[i]["name"].lower():
                is_book_found=True
                if self.books[i]["borrow"]==True:
                    print("sorry this book is already borrowed by someone else")
                else:
                    print("you successfuly borrowed this book")
                    self.books[i]["borrow"]=True
                    break
          
            else:
                is_book_found=False
        if is_book_found==False:
           print("sorry this book isn't in this library")
        else:
           pass
    def returnbook(self):
        return1=(input("what is the name of the book you are returning:"))
        is_book_found=False
        for i in range(len(self.books)):
            if return1.lower()==self.books[i]["name"].lower():
                is_book_found=True
                if self.books[i]["borrow"]==False:
                    print("you never borrowed this book")
                if self.books[i]["borrow"]==True:
                    print("you have successfully returned your book ")
                    self.books[i]["borrow"]=False
                    break

            else:
               is_book_found=False
        if is_book_found==False:
            print("this was never in the library")
    def viewall(self):
        for i in range(len(self.books)):
            print("***************************************")
            print(f'Book Title:{self.books[i]["name"]}')
            print(f'Book Author:{self.books[i]["author"]}')
            print(f'Borrowed:{self.books[i]["borrow"]}')
            print("*****************************************")

    
flag=True
mybooks=LibrarySystem(name="Aditya")
while(flag):
    print("Press 1: If you want to add a book to the library")
    print("Press 2: If you want to borrow a book from the library")
    print("Press 3: If you want to return a book back to the library")
    print("Press 4: If you want to view all books")
    print("Press 5: If you want to end code")
    question1=int(input("please choose an option"))
    if question1==1:
        mybooks.add()
        continue
    if question1==2:
        mybooks.borrow()
        continue
    if question1==3:
        mybooks.returnbook()
        continue
    if question1 == 4:
        mybooks.viewall()
        continue
    if question1 == 5:
        flag=False
    else:
        print("wrong choice")



    
       
              
           

    
            
            





        
    