def search_book_by_title_or_ISBN(books):
     search_item = input("Enter Title or ISBN number to search the book: ")
     for book in books:
          if search_item.lower() in book['title'].lower() or search_item in book['ISBN']:
                print(f"Found: {book['title']} - {book['ISBN']}")