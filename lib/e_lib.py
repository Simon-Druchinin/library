class E_lib:
    #books are given unique id
    def __init__(self):
        file = open(f'data/book_id.txt', 'r', encoding='utf-8')
        book_line = file.readline()
        file.close()

        self.book_id = book_line

    #returns a list with all existing books
    def book_list(self):
        books = []
        file = open(f'data/book_list.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close
        for line in lines:
            books.append(line)
        return books