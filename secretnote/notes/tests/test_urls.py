from django.test import SimpleTestCase
from django.urls import resolve, reverse
from notes.views import NotesDeleteView, NotesCreateView, NotesDetailsView, NotesListView, NotesUpdateView


class TestUrls(SimpleTestCase):
    
    def test_noteslist_url_resolves(self):
        url = reverse("notes.list")
        self.assertEquals(resolve(url).func.__name__, NotesListView.as_view().__name__)
        
    def test_notesnew_url_resolves(self):
        url = reverse("notes.new")
        self.assertEquals(resolve(url).func.__name__, NotesCreateView.as_view().__name__)
        
    def test_notesdetail_url_resolves(self):
        url = reverse("notes.detail", args=["id"])
        self.assertEquals(resolve(url).func.__name__, NotesDetailsView.as_view().__name__)
        
    def test_notesupdate_url_resolves(self):
        url = reverse("notes.update", args=["id"])
        self.assertEquals(resolve(url).func.__name__, NotesUpdateView.as_view().__name__)
        
    def test_notesdelete_url_resolves(self):
        url = reverse("notes.delete", args=["id"])
        self.assertEquals(resolve(url).func.__name__, NotesDeleteView.as_view().__name__)
        
