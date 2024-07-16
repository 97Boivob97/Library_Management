def backup_lent_books(lent_books):
    with open("lentbooks.csv", "wt") as fp:
        for lent in lent_books:
            line = f"{lent['title']},{lent['lender']}\n"
            fp.write(line)
    print("Backup Done!")
