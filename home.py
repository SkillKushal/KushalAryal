# from abc import ABC, abstractmethod
# class LibraryUser(ABC):
#     @abstractmethod
#     def borrow_book(self,book):
#         pass

#     @abstractmethod
#     def return_book(self,book):
#         pass

# class Book:
#     books = 3
#     def __init__(self, title, author, ISBN, is_available):
#           self.title = title
#           self.__author = author
#           self.__ISBN = ISBN
#           self.is_available =  True
    
#     def get_title(self):
#         return self.__title

#     def get_author(self):
#         return self.__author

#     def get_ISBN(self):
#         return self.__ISBN

#     def is_available(self):
#         return self.__is_available


#     def borrow(self):
#         if is_available == False:
#             print("The book is already borrowed")
#         else:
#             print("You can borrow the book")

#     def return_book(self):
#         if not self.__is_available:
#             self.__is_available = True
#             print(f"The book '{self.__title}' has been returned.")
#         else:
#             print(f"The book '{self.__title}' was not borrowed.")


# class Member(Book):
#     def __init__(self,name,member_id):
#         self.__name = name
#         self.__member_id = member_id
#         self.borrowed_books = []
        

#     def borrow_book(self,book:Book):
#         if book.is_available():
#              book.borrow()
#              self.borrowed_books.append(book)
#         else:
#             print("You should return the book")
            

#     def return_book(self,book:Book):
#         if book in self.borrowed_books:
#             book.return_book()
#             self.borrowed_books.remove(book)
#         else:
#             print("You haven't borrowed the book")



# class Staff(Member):
#     def __init__(self,name, member_id, positon):
#         super().__init__(name,member_id)
#         self.position = position


# class Librarian(Staff): 
#     super().__init__(self,name,member_id,position) 
#     Librarian.books = Librarian.books + 1



            



             





