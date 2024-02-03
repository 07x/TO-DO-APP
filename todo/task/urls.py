from django.urls import path
from .views import index, update_task,delete

urlpatterns = [
    path('',index,name='index',),
    path('update-task/<str:pk>/',update_task,name='update_task'),
    path('delete/<str:pk>/',delete,name='delete'),

]
