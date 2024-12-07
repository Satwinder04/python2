# create a class Library with a class variable total_books to keep track of total books in Library. Create a method to increase the total books when a new book is added

class Library:
    books = 0
    def total_books(self,books):
        self.books += books
    def display_info(self):
        print(f"Total number of books are {self.books}")

ob1 = Library()
ob1.total_books(10)
ob1.total_books(5)
ob1.total_books(12)
ob1.display_info()