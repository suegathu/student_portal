from django.urls import path
from .views import home, notes,NotesDetailView, delete_note, homework, update_homework, delete_homework, youtube, todo, update_todo, delete_todo, books, dictionary

urlpatterns = [
    path('', home, name='home'),
    path('notes/', notes, name='notes'),
    path('delete_note/<int:pk>', delete_note, name='delete-note'),
    path('notes_detail/<int:pk>', NotesDetailView.as_view(), name='notes-detail'),
    path('homework/', homework, name='homework'),
    path('update_homework/<int:pk>', update_homework, name='update-homework'),
    path('delete_homework/<int:pk>', delete_homework, name='delete-homework'),
    path('youtube/', youtube, name='youtube'),
    path('todo/', todo, name='todo'),
    path('update_todo/<int:pk>/', update_todo, name='update-todo'),
    path('delete_todo/<int:pk>/', delete_todo, name='delete-todo'),
    path('books/', books, name='books'),
    path('dictionary/', dictionary, name='dictionary'),
]
