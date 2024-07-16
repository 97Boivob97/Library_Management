
def return_book(books,lent_books):
     search_item = input("Enter the ISBN number of the book you want to return: ")
     for lent in lent_books:
          if search_item == lent['ISBN']:
               for book in books:
                     if book['ISBN'] == lent['ISBN']:
                             book['quantity'] += 1
                             lent_books.remove(lent)                 
                             print("Book has been returned successfully!")  
                             return lent_books
     print("Book not found in lent books!")  
     return lent_books