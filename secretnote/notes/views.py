from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Note
from .forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from cryptography.fernet import Fernet
from django.conf import settings


f = Fernet(settings.ENCRYPTION_KEY)


# @ratelimit(key='ip', rate='100/h')
class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


# @ratelimit(key='ip', rate='100/h')
class NotesDetailsView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"
    login_url = "/login"


# @ratelimit(key='ip', rate='100/h')
class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = "notes/note_form.html"
    success_url = "/secret/notes/"
    form_class = NoteForm
    login_url = "/login"

    def form_valid(self, form):
        note = form.save(commit=False)

        title = form.cleaned_data["title"]
        text = form.cleaned_data["text"]
        secret = form.cleaned_data["secret"]

        title_bytes = title.encode("utf-8")
        text_bytes = text.encode("utf-8")
        secret_bytes = secret.encode("utf-8")

        title_encrypted = f.encrypt(title_bytes)
        text_encrypted = f.encrypt(text_bytes)
        secret_encrypted = f.encrypt(secret_bytes)

        title_decoded = title_encrypted.decode("utf-8")
        text_decoded = text_encrypted.decode("utf-8")
        secret_decoded = secret_encrypted.decode("utf-8")

        note.title = title_decoded
        note.text = text_decoded
        note.secret = secret_decoded

        self.object = note
        self.object.user = self.request.user

        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @ratelimit(key='ip', rate='100/h')
class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = "notes/note_form.html"
    success_url = "/secret/notes/"
    form_class = NoteForm
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


# @ratelimit(key='ip', rate='100/h')
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = "/secret/notes/"
    template_name = "notes/note_delete.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()
