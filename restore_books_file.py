def restore_books(books):
     books.clear()
     with open("books.csv","r") as fp:
          for line in fp.readlines():
               line_split = line.strip().split(",")
               book={
                    "title":line_split[0],
                    "authors":line_split[1],
                    "ISBN":line_split[2],
                    "year":int(line_split[3]),
                    "price":float(line_split[4]),
                    "quantity":int(line_split[5])
               }
               books.append(book)
     print("Books has been restored!")