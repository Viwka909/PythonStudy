import json

books = [
    {"title": "Преступление и наказание", "author": "Достоевский", "year": 1866},
    {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967},
    {"title": "1984", "author": "Оруэлл", "year": 1949}
]

with open('books.json', 'w', encoding='utf-8') as file:
    json.dump(books, file, ensure_ascii=False, indent=2)