# from django.test import TestCase, Client
# from django.urls import reverse
# from notes.models import Note
# import json
# from notes.views import NotesDeleteView, NotesCreateView, NotesDetailsView, NotesListView, NotesUpdateView


# class TestViews(TestCase):
    
#     def setUp(self):
#         self.client = Client()
#         self.list_url = reverse("notes.list")
    
#     def test_notelist_view(self):
#         response = self.client.get(self.list_url)
#         print(response)
        
#         self.assertEquals(response.status_code, 302)
#         self.assertTemplateUsed(response, "notes/note_list.html")