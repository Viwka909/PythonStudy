from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Обычные URL блога
    path('api-auth/', include('rest_framework.urls')),  # API аутентификация
]
