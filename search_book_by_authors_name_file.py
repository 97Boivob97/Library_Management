def search_book_by_authorsname(books):
        search_item = input("Enter Authors name to search book: ")   
        found = False 
        for book in books:
              authors = book['authors']
              if isinstance(authors, list):
                    authors = ' '.join(authors)
              if search_item in authors.lower():
                   print(book['title'])
                   found = True
              if not found:
                     print("No books found by that author.")