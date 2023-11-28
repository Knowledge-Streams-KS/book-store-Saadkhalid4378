class Book:
    def __init__(self, title, author, catalogue, price, quantity):
        self.title = title
        self.author = author
        self.catalogue =catalogue
        self.price = price
        self.quantity = quantity


class Book_store:
    books = [ ]

    def add_book(self , book):
        self.books.append( book )
        print( " new book is added")
        print ( f" Title : { book.title } , Author : { book.author } , catalogue : { book.catalogue } , Price : { book.price} , Quantity { book.quantity} \n")

    def remove_book(self , title ):
        for book in self.books:
            if book.title.lower() == title.lower():
                # self.books.remove(book)
                x = self.books.index(book)
                self.books.pop(x)
                # if book == x:          #if book quantity is > 0 
                #     self.books.remove(book)
                print ( " book is removed \n")
                # else:
                #     print(" invalid indax :")    
            else:
                print( " inventory is empty \n")

    def search_by_title( self , title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print ( " book found \n " f"Title: { book.title} , Author : { book.author } ,  Quantity : {book.quantity} \n")
                x = self.books.index(book)
                print(f" index of book is : {x}")
                # self.x = book.index(book)
                # print(self.x)
            else:
                print( " inventory is empty \n")

    def search_by_author( self , author):
        for book in self.books:
            if book.author.lower() == author.lower():
                print ( " book found : \n " f"Title: { book.title} , Author : { book.author } \n")
            else:
                print( " inventory is empty ")

    def display_books( self , book):
        for book in self.books:
            if self.books:
                print ( " Here are all the books : \n" f"Title: { book.title } , Author : { book.author } , catalogue : { book.catalogue } , Price : { book.price} , Quantity { book.quantity} ")
                x = self.books.index(book)
                print(f" index of book is : {x}")
            else :
                print ( " no book is found \n")
    # def user_detail (self , user):
    #     for user in 

    
class User ():
    def __init__(self, name , age , address):
        self.name = name 
        self.age = age
        self.address = address
        self.Book_collection = []
        
    def buy_book( self ,  book ):
        # for book in book_store.books:
        #     if book in self.Book_collection:
        #         print()
        #     elif book.title.lower() == title.lower():
                self.remove_book = Book_store()
                self.remove_book.remove_book(book)
                self.Book_collection.append(book)
                print( f" book is sold  to user : {book.title},  " )
                    # self.books.remove(book)
                print( " book removed from store :")
            # else:
            #     print(" no book found ")
    # def buy_book( self , title , book_store  ):
    #     for book in book_store.book:
    #         if book.title.lower() == title.lower():
    #             self.Book_collection.append(book)
    #             print( f" book is sold  to user : , title : {book.title} " )
            # else:
            #     print(" no book found ")
    def user_book_collection(self):
        if self.Book_collection:
            print(" user book collection list : ")
            for book in self.Book_collection:
                print (f"Name : { self.name}")
        else:
            print( " no book found")


def main ():
    while (True):
        book_store = Book_store ()
        # user = User()
        print ( "Chose the related task. ")
        print ( " For adding book press 1 ")
        print ( " For removing book press 2 ")
        print ( " Search book by title  3 ")
        print ( " Search book by author 4 ")
        print ( " Display all books in inventory 5 ")
        print ( " For buying book 6 ")
        print ( " Display user books 7 ")
        print ( " Exit from inventory 8 ")

        chose = input ( "  Type your choise :")

        if chose == "1":
            a = input ( " Title of book : ")
            b = input ( " Author of book : ")
            c = input ( " Catalogue of book :")
            d = input ( " Price of book : ")
            e = input ( " Quantity of book : ")
            book1 = Book ( a,b,c,d,e)
            book_store.add_book(book1)

        elif  chose == "2":
            a = input (" title of book  ")
            book_store.remove_book(a)

        elif chose == "3":
            a = input ( " search by title : ")
            book_store.search_by_title(a)

        elif chose == "4":
            a = input ( " search by author : ")
            book_store.search_by_author(a)

        elif chose == "5":
            #a = input ( " display all the book in inventory :")
                book_store.display_books(book=Book)

        elif chose == "6":
            a = input(" user name : ")
            b = input(" user age  :")
            c = input(" user address : ")
            to_buy_book = input ("enter book title to buy book : ")
            user = User(a,b,c)
            user.buy_book(to_buy_book)
            # user.user_book_collection()

        elif chose == "7":
            a = print(" user name : ")
            b = print(" user age  :")
            c = print(" user address : ")
            user.user_book_collection()

        elif chose == "8":
            print (" Inventory Closed")
            break

        else :
            print ( " invalid choice")

main() 


# class User ():
#     def __init__(self, name , age , address ):
#         self.name = name 
#         self.age = age
#         self.address = address
#         self.Book_collection = []

#     def buy_book( self ,  book):
#         for book in self.books:
#             self.Book_collection.append(book)
#             print( " book is sold  to user :")
#         else:
#             print( " no book is sold :")


        
# class User ():
#     def __init__(self, name , age , address):
#         self.name = name 
#         self.age = age
#         self.address = address
# class User_books():
#     U_books = []
#     def add_user( self , user):
#         self.U_books.append(user)
#         print( " user is entered" )
#     def buy_book( self , book ):
#         self.U_books.append(book)
#         print( " book is entered ")
#     def user_book_display(self):
#         for book in self.U_books:
#             print(book)

# user_books = User_books()

# print ( " enter your choice ")
# print ( " to enter user type 1")
# print ( " for buying book type 2")
# print ( " display all user books 3")
# chose = input ( " type your choice ")
# if chose == "1":
#     a = input (" enter user details ")
#     b = input (" enter user age ")
#     c = input (" enter user address ")
#     user1 = User(a,b,c)
#     u_book = user_books.add_user(user1)