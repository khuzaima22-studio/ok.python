class Library:
    def __init__(self, List, name) :
        self.booklist = ['Lord of Rings','Great Expectations','Beloved','Harry Potter']
        
        self.name = name
        self.lendict = {}

    def displaybooks (self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook (self, user, book):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print("Database of Lender-book is updated. Now you can take the book")
        else:
            print(f"Book is already being used by {self.lendict[book]}")

    def addbook(self, book):
            self.booklist.append(book)
            print("Book has been added in to the book list")

    def returnbook(self, book):
            self.lendict.pop(book)

if __name__ == '__main__':
    Khuzaima = Library(['Lord of Rings','Great Expectations','Beloved','Harry Potter'], "Magical books by Khuzaima")
    while(True):
        print(f"Welcome to the Library of {Khuzaima.name}. Enter your favourite book to continue")
        print("1. Display a book")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = input()

        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            Khuzaima.displaybooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            Khuzaima.lendbook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            Khuzaima.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            Khuzaima.returnbook(book) 

        else:
            print("Not a valid option")

        print("Press C to continue and E to Exit")
        user_choice2 = ""
        while(user_choice2!= "C" and user_choice2!= "E"):
            user_choice2 = input()
            if user_choice2 == "E":
                exit()

            elif user_choice2 == "C":
                continue    

                   


    

                            