from django.contrib import admin
from django.urls import path, include
from tasks.views import main_page_view

urlpatterns = [
    path('', main_page_view, name='main_page'),
    path('admin/', admin.site.urls),
    path('api/v1/tasks/', include('tasks.urls')),
]