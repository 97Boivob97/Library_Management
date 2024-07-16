def backup_books(books):
     with open("books.csv","wt") as fp:
          for book in books:
               line = f"{book['title']},{book['authors']},{book['ISBN']},{book['year']},{book['price']},{book['quantity']}\n" 
               fp.write(line)
     print("Backup Done!")