import os
import shutil
#import book template
from .e_lib import E_lib

#books are given name, chapter_name and text
class Book(E_lib):
    def __init__(self, name, chapter_name, text):
        E_lib.__init__(self)
        self.name = name
        self.chapter_name = chapter_name
        self.text = text

    def give_id(self):
        books = self.book_list()

        item = books[len(books)-1].replace('\n', '')

        file = open(f'data/{item}/info.txt', 'r', encoding='utf-8')
        book_line = file.readline()
        file.close()

        book_line = int(book_line) + 1

        file = open(f'data/book_id.txt', 'w', encoding='utf-8')
        file.write(str(book_line))
        file.close()

    #create in '/data/' folder with book's name, where is placed file with info about book
    def write_to_lib(self):
        books = self.book_list()
        if self.name + '\n' not in books:
            os.mkdir(f'data/{self.name}')
            self.create_a_book()
            file = open(f'data/{self.name}/info.txt', 'w', encoding='utf-8')
            file.write(f'{str(self.book_id)}\n')
            chapters = self.chapter_amount()
            file.write(str(chapters))
            file.close()

            file = open(f'data/book_list.txt', 'a', encoding='utf-8')
            file.write(self.name)
            file.write('\n')
            file.close()
            self.give_id()

    #returns a list with all existing books
    def book_list(self):
        books = []
        file = open(f'data/book_list.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close
        for line in lines:
            books.append(line)
        return books
    
    #delete a book
    def delete_book(self, name):
        shutil.rmtree(f'data/{name}')

        file = open(f'data/book_list.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close

        file = open(f'data/book_list.txt', 'w', encoding='utf-8')
        for line in lines:
            if line != name + '\n':
                file.write(line)
        file.close()

    #change book's name
    def rename_book(self, old_name, new_name):
        os.renames(f'data/{old_name}', f'data/{new_name}')

        file = open(f'data/book_list.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close

        file = open(f'data/book_list.txt', 'w', encoding='utf-8')
        for line in lines:
            if line == old_name + '\n':
                file.write(new_name + '\n')
            else:
                file.write(line)
        file.close()

    #create a composition with text and chapters
    def create_a_book(self):
        file = open(f'data/{self.name}/text.txt', 'w', encoding='utf-8')
        file.write(f'Глава: "{self.chapter_name}"\n')
        file.write(f'{self.text}\n')
        file.close()

        file = open(f'data/{self.name}/chapters_list.txt', 'w', encoding='utf-8')
        file.write(f'Глава: "{self.chapter_name}"\n')
        file.close

    #add new chapter
    def extend_book(self, name, chapter_name, text):
        file = open(f'data/{name}/text.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()

        file = open(f'data/{name}/text.txt', 'w', encoding='utf-8')
        for line in lines:
            file.write(line)
        file.write(f'Глава: "{chapter_name}"\n')
        file.write(f'{text}\n')
        file.close()
        
        #refresh the list of chapters
        file = open(f'data/{name}/chapters_list.txt', 'a', encoding='utf-8')
        file.write(f'Глава: "{chapter_name}"\n')
        file.close()

        #change amount of chapters(+1)
        file = open(f'data/{name}/info.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()

        lines[1] = int(lines[1]) + 1
        file = open(f'data/{name}/info.txt', 'w', encoding='utf-8')
        for line in lines:
            file.write(str(line))
        file.close()

    #delete any chapter user wants    
    def delete_chapter(self, name, chapter_name):
        try:
            chapters = self.chapters_list()
            file = open(f'data/{name}/text.txt', 'r', encoding='utf-8')
            lines = file.readlines()
            file.close()

            start = chapters.index(f'Глава: "{chapter_name}"\n')
            end = start + 1

            start_line = lines.index(f'Глава: "{chapter_name}"\n')
            end_line = lines.index(chapters[end])

            file = open(f'data/{name}/text.txt', 'w', encoding='utf-8')
            for line in lines:
                if line == chapters[start]:
                    for i in range(start_line, end_line):
                        lines[i] = ''
                else:
                    file.write(line)
            file.close()
        except IndexError:
            chapters = self.chapters_list()
            file = open(f'data/{name}/text.txt', 'r', encoding='utf-8')
            lines = file.readlines()
            file.close()

            start_line = lines.index(f'Глава: "{chapter_name}"\n')

            file = open(f'data/{name}/text.txt', 'w', encoding='utf-8')
            for line in lines:
                if line == chapters[start]:
                    for i in range(start_line, len(lines)):
                        lines[i] = ''
                else:
                    file.write(line)
            file.close()

        #refresh the list of chapters
        file = open(f'data/{self.name}/chapters_list.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close

        file = open(f'data/{self.name}/chapters_list.txt', 'w', encoding='utf-8')
        for line in lines:
            if line != f'Глава: "{chapter_name}"\n':
                file.write(line)
        file.close

        #change amount of chapters(-1)
        file = open(f'data/{name}/info.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()

        lines[1] = int(lines[1]) - 1
        file = open(f'data/{name}/info.txt', 'w', encoding='utf-8')
        for line in lines:
            file.write(str(line))
        file.close()
    
    #returns a list of all chapters of the book
    def chapters_list(self):
        chapters = []
        file = open(f'data/{self.name}/chapters_list.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close
        for line in lines:
            chapters.append(line)
        return chapters

    #count amount of chapters
    def chapter_amount(self):
        chapters = self.chapters_list()
        chapters = len(chapters)
        return chapters
    
    #change name of the chapter
    def change_chapter_name(self, name, chapter_old, chapter_new):
        file = open(f'data/{name}/text.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()

        file = open(f'data/{name}/text.txt', 'w', encoding='utf-8')
        for line in lines:
            if line == f'Глава: "{chapter_old}"\n':
                line = f'Глава: "{chapter_new}"\n'
            file.write(line)
        file.close()

        #refresh the list of chapters
        file = open(f'data/{self.name}/chapters_list.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        file.close

        file = open(f'data/{self.name}/chapters_list.txt', 'w', encoding='utf-8')
        for line in lines:
            if line == f'Глава: "{chapter_old}"\n':
                line = f'Глава: "{chapter_new}"\n'
            file.write(line)
        file.close

    #rewrite chosen chapter
    def rewrite_chapter(self, name, chapter, new_text):
        try:
            chapters = self.chapters_list()
            file = open(f'data/{name}/text.txt', 'r', encoding='utf-8')
            lines = file.readlines()
            file.close()

            start = chapters.index(f'Глава: "{chapter}"\n')
            end = start + 1

            start_line = lines.index(f'Глава: "{chapter}"\n')
            end_line = lines.index(chapters[end])

            start_line += 1

            progress = True

            file = open(f'data/{name}/text.txt', 'w', encoding='utf-8')
            for line in lines:
                if line == lines[start_line] and progress == True:
                    for i in range(start_line, end_line):
                        lines[i] = ''
                    else:
                        for ln in new_text:
                            file.write(f'{ln}\n')
                        progress = False
                else:
                    file.write(line)
            file.close()
        except IndexError:
            chapters = self.chapters_list()
            file = open(f'data/{name}/text.txt', 'r', encoding='utf-8')
            lines = file.readlines()
            file.close()

            start_line = lines.index(f'Глава: "{chapter}"\n')
            start_line += 1
            print(start_line)

            file = open(f'data/{name}/text.txt', 'w', encoding='utf-8')
            for line in lines:
                if line == lines[start_line]:
                    for i in range(start_line, len(lines)):
                        lines[i] = ''
                else:
                    file.write(line)
            for line in new_text:
                file.write(f'{line}\n')
            file.close()

    #looks for info about books
    @staticmethod
    def read_from_files(dir_name, files):
        books = []
        for file_name in files:
            if file_name == 'info.txt':
                file = open(dir_name + file_name, 'r', encoding='utf-8')
                lines = file.readlines()
                file.close()

                books.append(lines[0])
                books.append(lines[1])
        return books

    #parse the data folder and output all information about books
    def all_info(self):
        #list of created books
        books = self.book_list()
        info_about_books = []

        for item in books:
            item = item.replace('\n', '')
            current_path = os.getcwd()
            data_dir = current_path + '/data/' + f'/{item}/'
            data_files = os.listdir(data_dir)

            books = Book.read_from_files(data_dir, data_files)
            books[0] = books[0].replace('\n', '')

            info_about_books.append(f'Название: {item}')
            info_about_books.append(f'id: {books[0]}')
            info_about_books.append(f'Количество глав: {books[1]}')
            info_about_books.append('')

        return info_about_books