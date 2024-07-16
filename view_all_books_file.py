def view_all_books(books):
    for book in books:
        print(book['title'],(book['authors']), book['ISBN'], book['year'], book['price'], book['quantity'], sep=" | ")