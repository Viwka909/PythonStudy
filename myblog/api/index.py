# # api/index.py
# import os
# import sys
# from django.core.wsgi import get_wsgi_application

# # Добавьте путь к проекту в sys.path
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # Установите переменные окружения Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

# # Получите Django application
# application = get_wsgi_application()

# # Обработчик для Vercel Serverless Functions
# def handler(request, response):
#     """
#     Обработчик запросов для Vercel
#     """
#     from django.http import HttpRequest, HttpResponse
#     from django.core.handlers.wsgi import WSGIHandler
    
#     # Создаем WSGI handler
#     wsgi_handler = WSGIHandler()
    
#     # Конвертируем Vercel request в Django request
#     django_request = HttpRequest()
#     django_request.path = request.path
#     django_request.method = request.method
#     django_request.META = request.headers
    
#     # Обрабатываем запрос
#     django_response = wsgi_handler(django_request)
    
#     # Возвращаем ответ
#     response.status = django_response.status_code
#     for key, value in django_response.headers.items():
#         response.set_header(key, value)
#     response.send(django_response.content)
    
#     return response

# # Альтернативный простой вариант (если выше не работает)
# def simple_handler(request, response):
#     """
#     Простой обработчик для тестирования
#     """
#     response.status(200).send("Hello from Django on Vercel!")
#     return response

# # Для локального тестирования
# if __name__ == "__main__":
#     from django.core.management import execute_from_command_line
#     execute_from_command_line(sys.argv)