from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NotesListView.as_view(), name="notes.list"),
    path('notes/new/', views.NotesCreateView.as_view(), name="notes.new"),
    path('notes/<str:pk>/', views.NotesDetailsView.as_view(), name="notes.detail"),
    path('notes/<str:pk>/edit/', views.NotesUpdateView.as_view(), name="notes.update"),
    path('notes/<str:pk>/delete/', views.NotesDeleteView.as_view(), name="notes.delete"),
]