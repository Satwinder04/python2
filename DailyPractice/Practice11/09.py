# Create a class book with a method book_info(self,title,author="Unknown") to print the title and author of the book. call the method with and without argument.

class Books:
    def book_info(self,title,author="Unknown"):
        print(f"Title:{title} Author:{author}")

book = Books()
book.book_info("The Rich Dad","THe knownnn")
book.book_info("Helelo worldjj")

