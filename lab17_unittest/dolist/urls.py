from django.urls import path
from . import views

urlpatterns = [
    # load page of the app will be sent to the index.html
    path('', views.index, name='index'),
    path('add', views.addTodoitem, name="add"),

    # add a path for completed items in our list
    path('completed/<int:todo_id>/', views.completedTodo, name='completed'),

    # delete tasks that are marked as complete 
    path('deletecompleted', views.deletecompleted, name='deletecompleted'),

    # delete all tasks
    path('deleteall', views.deleteAll, name = 'deleteall'),
]