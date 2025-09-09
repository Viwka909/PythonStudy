import requests 
import json     
import time      
from datetime import datetime


class TaskManager:
    
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.todos_url = f"{self.base_url}/todos"  # endpoint для задач
        self.users_url = f"{self.base_url}/users"  # endpoint для пользователей
    
    def get_user_info(self, user_id):
        """Получить информацию о пользователе по ID"""
        response = requests.get(f"{self.users_url}/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка при получении информации о пользователе {user_id}")
            return None
    
    def get_user_tasks(self, user_id):
        """Получить задачи пользователя с анализом статусов"""
        response = requests.get(f"{self.todos_url}?userId={user_id}")
        if response.status_code != 200:
            print(f"Ошибка при получении задач пользователя {user_id}")
            return None
            
        tasks = response.json()
        
        # Разделяем задачи по статусу выполнения
        completed = [task for task in tasks if task['completed']]
        pending = [task for task in tasks if not task['completed']]
        
        return {
            'total': len(tasks),
            'completed': len(completed),
            'pending': len(pending),
            'tasks': tasks
        }
    
    def print_user_report(self, user_id):
        """Создание комплексного отчета по пользователю"""
        user_info = self.get_user_info(user_id)
        if not user_info:
            print(f"Пользователь с ID {user_id} не найден")
            return
        
        tasks_info = self.get_user_tasks(user_id)
        if not tasks_info:
            print(f"Не удалось получить задачи пользователя {user_id}")
            return
        
        print(f"\n📊 ОТЧЕТ ПО ПОЛЬЗОВАТЕЛЮ:")
        print(f"👤 {user_info.get('name', 'Неизвестно')} ({user_info.get('email', 'Нет email')})")
        print(f"📋 Всего задач: {tasks_info['total']}")
        print(f"✅ Выполнено: {tasks_info['completed']}")
        print(f"⏳ Осталось: {tasks_info['pending']}")
        
        # Показываем 3 ближайшие невыполненные задачи
        pending_tasks = [task for task in tasks_info['tasks'] if not task['completed']]
        if pending_tasks:
            print(f"\n🎯 Ближайшие задачи:")
            for task in pending_tasks[:3]:
                print(f"   ⏳ {task['title'][:50]}...")
    
    def create_task(self, user_id, title, completed=False):
        """Создать новую задачу для пользователя"""
        task_data = {
            'userId': user_id,
            'title': title,
            'completed': completed
        }
        
        response = requests.post(self.todos_url, json=task_data)
        if response.status_code == 201:  # 201 Created
            return response.json()
        else:
            print(f"Ошибка при создании задачи: {response.status_code}")
            return None

# Использование менеджера задач
def demo_task_manager():
    """Демонстрация работы менеджера задач"""
    manager = TaskManager()
    
    # Получаем отчет для пользователя с ID 1
    print("=== ОТЧЕТ ПО ПОЛЬЗОВАТЕЛЮ 1 ===")
    manager.print_user_report(1)
    
    # Создаем новую задачу
    print("\n=== СОЗДАНИЕ НОВОЙ ЗАДАЧИ ===")
    new_task = manager.create_task(1, "Изучить Python API и создать свой проект", False)
    if new_task:
        print(f"🆕 Создана задача: {new_task['title']}")
        print(f"   ID задачи: {new_task.get('id', 'N/A')}")
        print(f"   Статус: {'✅ Выполнена' if new_task['completed'] else '⏳ В процессе'}")

# Запуск демонстрации
if __name__ == "__main__":
    demo_task_manager()