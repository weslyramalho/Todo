
from django.contrib import admin
from django.urls import path
from app.views import addTodo, home




urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-todo/', addTodo, name='addtodo'),
    path('', home)
    #path('', views.index, name="todo"),
    #path("", include("app.urls")),
    #path('del/<str:item_id>', views.remove, name="del"),
]

