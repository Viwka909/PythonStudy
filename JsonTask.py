import json
#1)Создай JSON-файл с данными о книгах (название, автор, год издания)
#2)Напиши функцию, которая читает этот файл и возвращает книги после указанного года

books = [
    {"title": "Преступление и наказание", "author": "Достоевский", "year": 1866},
    {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967},
    {"title": "1984", "author": "Оруэлл", "year": 1949}
]

with open('books.json', 'w', encoding='utf-8') as file:
    json.dump(books, file, ensure_ascii=False, indent=2)

def find_books_after_year(filename, year):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            books = json.load(file)
            result = []
            for book in books:
                if book['year'] > year:
                    result.append(book)
            return result
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return []

# Использование
recent_books = find_books_after_year('books.json', 1950)
for book in recent_books:
    print(f"{book['title']} ({book['year']})")