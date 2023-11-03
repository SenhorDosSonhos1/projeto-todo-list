from django.urls import path
from . import views 

urlpatterns = [
    path('', views.task, name='task'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('update_task/<int:id>', views.update_task, name='update_task'),
    path('read_task/<int:id>', views.read_task, name='read_task'), 
]
