from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Item(ABC):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
        self.due_date = None
    
    @abstractmethod
    def get_loan_period(self):
        pass
    
    def borrow(self):
        if self.is_available:
            self.is_available = False
            self.due_date = datetime.now() + timedelta(days=self.get_loan_period())
            return True
        return False
    
    def return_item(self):
        self.is_available = True
        self.due_date = None
    
    def is_overdue(self):
        if self.due_date and datetime.now() > self.due_date:
            return True
        return False

class Book(Item):
    def get_loan_period(self):
        return 30  # 30 дней для книг

class Magazine(Item):
    def get_loan_period(self):
        return 7  # 7 дней для журналов

class Library:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def find_by_title(self, title):
        return [item for item in self.items if item.title.lower() == title.lower()]
    
    def get_overdue_items(self):
        return [item for item in self.items if item.is_overdue()]

# Использование
library = Library()

book = Book("Преступление и наказание", "Достоевский", 1866)
magazine = Magazine("National Geographic", "Various", 2024)

library.add_item(book)
library.add_item(magazine)

book.borrow()
print(f"Книга должна быть возвращена до: {book.due_date}")
print(f"Просрочена: {book.is_overdue()}")