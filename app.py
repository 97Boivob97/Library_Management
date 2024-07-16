
import create_book_file
import view_all_books_file
import search_book_by_title_or_ISBN_file
import search_book_by_authors_name_file
import remove_book_file
import lent_books_file
import view_lent_books_file
import return_books_file
import backup_books_file
import backup_lent_books_file
import restore_books_file
books = [
 #{
    #"title" : "To Kill a mocking bird",
    #"authors" : "Harper Lee",
    #"ISBN" : "101",
    #"year" : 2000,
   #"price" : 500,
    #"quantity" : 100
 #},
 #{
    #"title" : "Hane Eyre",
    #"authors" : "Charlote Bronte",
    #"ISBN" : "102",
    #"year" : 2001,
    #"price" : 300,
    #"quantity" : 50 
 #},
  #{
    #"title" : "Hane Eyre",
    #"authors" : "Charlote Bronte",
    #"ISBN" : "103",
    #"year" : 2001,
    #"price" : 300,
    #"quantity" : 50 
 #}
]
lent_books = []             
print("Welcome!")
menu = """
  1. Add Book
  2. View All Books
  3. Search book by its title or ISBN
  4. Search book by its authors name
  5. Remove a book
  6. Lend a book
  7. View all the lent books
  8. Return a book
  9. Backup Books
  10. Backup Lent Books
  11. Restore Books
  0. Press 0 to exit
"""
while True:
     print(menu)
     choice = input("Enter your choice: ")
     if choice == "1":
          books = create_book_file.create_book(books)
          backup_books_file.backup_books(books)
     elif choice == "2":
          view_all_books_file.view_all_books(books)
     elif choice == "3":
          search_book_by_title_or_ISBN_file.search_book_by_title_or_ISBN(books)
     elif choice == "4":
          search_book_by_authors_name_file.search_book_by_authorsname(books)
     elif choice == "5":
          books=remove_book_file.remove_book(books)
          backup_books_file.backup_books(books)
     elif choice ==  "6":
          lent_books=lent_books_file.lent_book(books,lent_books)
     elif choice == "7":
            view_lent_books_file.view_lent_books(lent_books)                   
     elif choice == "8":
          lent_books=return_books_file.return_book(books,lent_books)
          backup_books_file.backup_books(books)
     elif choice == "9":
          backup_books_file.backup_books(books)
     elif choice == "10":
          backup_lent_books_file.backup_lent_books(lent_books)
     elif choice == "11":
          restore_books_file.restore_books(books)
          backup_books_file.backup_books(books)
     elif choice == "0":
          print("Thank you!")
          break
     else:
          print("Invalid Choice!! Please try Again!")
          

