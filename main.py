import os
#import book template
from lib.e_lib import E_lib
#import daughterly class
from lib.book import Book

def book_creation(name):
    book = Book(name, '', '')
    books = book.book_list()

    if name + '\n' in books:
        return ('Такая книга уже существует, но вы можете поработать с главами этой книги :)')

    else:
        chapter = input('Введите название первой главы: ')
        first_chapter_text = ''

        loop = True

        while loop:
            first_chapter_text += input('Введите текст главы(переход на следующую строку Enter):\n') + '\n'
            dont_write = input('Если хотети закончить напишите 1, иначе Enter -- ')
            if dont_write == '1':
                loop = False

        #create a new book
        book = Book(name, chapter, first_chapter_text)
        book.write_to_lib()
        return f'Вы создали книгу {name} с первой главой {chapter}'

def what_to_do(user_choice):
    if int(user_choice) < 8:
        name = input('Введите название книги: ')
        book = Book(name, '', '')
        books = book.book_list()

        if user_choice == '1':
            return book_creation(name)

        elif user_choice == '2':
            if name + '\n' not in books:
                return('Такой книги не существует')
            else:
                chapter_name = input('Введите название главы: ')
                chapter_text = input('Введите текст главы(переход на следующую строку Enter):\n')
                loop = True
                while loop:
                    chapter_text += input('Введите текст главы(переход на следующую строку Enter):\n') + '\n'
                    dont_write = input('Если хотети закончить напишите 1, иначе Enter -- ')
                    if dont_write == '1':
                        loop = False
                book.extend_book(name, chapter_name, chapter_text)
                return f'Вы добавили главу {chapter_name}'

        elif user_choice == '3':
            if name + '\n' in books:
                book.delete_book(name)
                return f'Вы удалили книгу {name}'
            else:
                return 'Такой книги не существует'

        elif user_choice == '4':
            if name + '\n' in books:
                new_name = input('Введите новое название книги: ')
                book.rename_book(name, new_name)
                return f'Вы изменилии название книги "{name}" на название "{new_name}"'
            else:
                return('Такой книги не существует')
        
        elif user_choice == '5':
            if name + '\n' in books:
                old_chapter = input('Введите название главы, которое хотите изменить: ')
                new_chapter = input('Введите новое название главы: ')
                book.change_chapter_name(name, old_chapter, new_chapter)
                return f'Вы изменили название главы "{old_chapter}" на "{new_chapter}"'

        elif user_choice == '6':
            if name + '\n' in books:
                chapter = input('Введите название главы, которуе хотите изменить: ')
                new_text = ''
                loop = True
                while loop:
                    new_text += input('Введите текст этой главы(переход на следующую Enter):\n') + '\n'
                    dont_write = input('Если хотети закончить напишите 1, иначе Enter -- ')
                    if dont_write == '1':
                        loop = False
                book.rewrite_chapter(name, chapter, new_text.split('\n'))
                f'Вы перезаписали главу "{chapter}"'
            else:
                return('Такой книги не существует')

        elif user_choice == '7':
            if name + '\n' in books:
                chapter = input('Введите название главы, которую хотите удалить: ')
                book.delete_chapter(name, chapter)
                return f'Вы удалили главу {chapter}'
            else:
                return('Такой книги не существует')

    elif user_choice == '8':
        book = Book('', '', '')
        return book.all_info()

    elif user_choice == '9':
        loop = False
        return loop
    
    else:
        return('Такой команды не существует')


loop = True
message = ''

print('Добро пожаловать в книжный редактор!')
print('С чего хотите начать?)')

while loop:
    print('Выберите любой пункт:')

    user_choice = input('''
    1. Создать книгу
    2. Добавить главу к книге 
    3. Удалить книгу
    4. Изменить название книги
    5. Изменить название главы
    6. Перезаписать главу
    7. Удалить главу
    8. Вывести информацию о всех существующих книгах
    9. Выйти из редактора
    ''')

    if user_choice == '8':
        message = what_to_do(user_choice)
        for item in message:
            print(item)

    elif user_choice == '9':
        loop = what_to_do(user_choice)

    else:
        message = what_to_do(user_choice)
        print(message)