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

add_mood_entry()