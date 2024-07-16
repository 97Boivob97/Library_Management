                  
def view_lent_books(lent_books):
    for lent in lent_books:
        print(f"Title: {lent['title']}, ISBN: {lent['ISBN']}, lender: {lent['lender']}")   