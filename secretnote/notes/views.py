from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    login_url = "/admin"
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
    
class NotesDetailsView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = "note"
    login_url = "/admin"
    
    def get_queryset(self):
        return self.request.user.notes.all()


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Note
    success_url = '/secret/notes/'
    form_class = NoteForm
    login_url = "/admin"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())
    
    
class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    success_url = '/secret/notes/'
    form_class = NoteForm
    login_url = "/admin"
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/secret/notes/'
    template_name = 'notes/note_delete.html'
    login_url = "/admin"
    
    def get_queryset(self):
        return self.request.user.notes.all()