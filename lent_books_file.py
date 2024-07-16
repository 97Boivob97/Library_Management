def lent_book(books,lent_books):
         search_item = input("Enter the ISBN number to search book you want to lent: ")
         for book in books:
              if search_item == book['ISBN']:
                   if book['quantity'] > 0:
                        lender = input("Enter the name of the person who wants to lend this book: ")
                        book["quantity"] -= 1
                        lent_books.append(
                             {
                                  "title": book['title'],
                                  "ISBN":book['ISBN'],
                                  "lender":lender
                             }
                        )
                        print("Book has been lent successfully!")
                        return lent_books
                   else:
                        print("not enough books are available to lend!")
                        return lent_books
              print("Book not found!")
              return lent_books