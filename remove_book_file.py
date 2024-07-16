def remove_book(books):
    ISBN = input("Enter the ISBN number of the book you want to remove: ")

    found = False
    for book in books:
        if book['ISBN'] == ISBN:
            books.remove(book)
            found = True
            print(f"Book with ISBN {ISBN} has been removed successfully!")
            break
    if not found:
        print(f"Error: Book with ISBN {ISBN} not found in the library.")
    return books