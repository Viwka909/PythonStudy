import json
from datetime import datetime


def add_mood_entry():
    try:
        name = input("Ваше имя: ")
        mood = int(input("Настроение (1-10): "))
        comment = input("Комментарий: ")
        
        entry = {
            "date": str(datetime.now()),
            "name": name,
            "mood": mood,
            "comment": comment
        }
        
        
        try:
            with open('mood_diary.json', 'r', encoding='utf-8') as file:
                entries = json.load(file)
        except FileNotFoundError:
            entries = []
        
        entries.append(entry)
        
        with open('mood_diary.json', 'w', encoding='utf-8') as file:
            json.dump(entries, file, ensure_ascii=False, indent=2)
            
        print("Запись добавлена успешно!")
        
    except ValueError:
        print("Ошибка: Настроение должно быть числом!")
    except Exception as e:
        print(f"Ошибка: {e}")

def calculate_average_mood(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            diary = json.load(file)
            result = 0
            entries = 0
            for entry in diary:
                entries += 1
                result+=entry['mood']
            return result/entries
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return []

add_mood_entry()
print("Среднее настроение - ",calculate_average_mood('mood_diary.json'))
