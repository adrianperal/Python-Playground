class Book:
    # TODO
    def __init__(self, title, author, pub_year, n_copies):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.n_copies = n_copies
        
        with open('id_counter.txt', 'r') as file:
            counter = []
            for id in file.readlines():
                counter.append(id.strip("\n").split(":"))
            book_id = int(counter[0][3]) + 1
        with open('books.txt', 'a') as file, open('id_counter.txt', 'w') as file2:
            file2.write(f"user_id:{counter[0][1]}:book_id:{book_id}")
            file.write(f"{book_id}:{self.title}:{self.author}:{self.pub_year}:{self.n_copies}\n")
    
    def borrow_book(self):
        book_exists = 0
        with open('books.txt', 'r') as file:
            book_list = []
            for book in file.readlines():
                book_list.append(book.strip("\n").split(":"))
        for book in book_list:
            is_available = int(book[4])
            if is_available > 0:
                print(f"Book ID: {book[0]}: {book[1]} by {book[2]} published in {book[3]}")
        book_id = input("Enter the book ID: ")            
        for book in book_list:
            if book[0] == book_id:
                book_exists = 1
                book[4] = int(book[4])
                if book[4] > 0:
                    book[4] -= 1
                    print(f"{book[4]} copies left.")
                else:
                    print("Book out of stock.")
        if book_exists == 1:
            with open('books.txt', 'w') as file:
                for book in book_list:
                    file.write(f"{book[0]}:{book[1]}:{book[2]}:{book[3]}:{book[4]}\n")
        else:
            print("Book not found!")