def create_book(books):
    title = input("Enter the title of the book: ")
    n = input("How many authors are here for this book: ")
    n = int(n)
    authors = []
    for i in range(0,n):
          author = input(f"Enter the {i+1}st author name of the book: ")
          authors.append(author)
    ISBN = input("Enter the ISBN number of the book: ")
    year = input("Enter the publising year of the book: ")
    year = int(year)
    while True:
         try:
              price=input("Enter the price of the book: ")
              price = float(price)
              break
         except ValueError:
              print("Error: Price should be a floating-point number. Please enter a valid price.")

    quantity = input("Enter the quantity of the book: ")
    quantity = int(quantity)
    book = {
        "title":title,
        "authors":authors,
        "ISBN":ISBN,
        "year":year,
        "price":price,
        "quantity":quantity
    }
    books.append(book)
    print("Book has been added successfully!")
    return books