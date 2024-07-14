from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm

class NotesListView(ListView):
    model = Note
    context_object_name = "notes"
    
class NotesDetailsView(DetailView):
    model = Note
    context_object_name = "note"


class NotesCreateView(CreateView):
    model = Note
    success_url = '/secret/notes/'
    form_class = NoteForm
    
class NotesUpdateView(UpdateView):
    model = Note
    success_url = '/secret/notes/'
    form_class = NoteForm
    
class NotesDeleteView(DeleteView):
    model = Note
    success_url = '/secret/notes/'
    template_name = 'notes/note_delete.html'