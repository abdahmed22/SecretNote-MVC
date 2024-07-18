from django.test import TestCase, Client
from django.urls import reverse
from notes.models import Note
from django.contrib.auth.models import User
from django.utils import timezone
from notes.views import NotesDeleteView, NotesCreateView, NotesDetailsView, NotesListView, NotesUpdateView


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.note1 = Note.objects.create(
            title = 'secret note 1',
            text = 'secret note 1 secret note 1 secret note 1 secret note 1',
            secret = 'secret1',
            destruction_date = timezone.now(),
            user = self.user
        )
        self.note2 = Note.objects.create(
            title = 'gAAAAABmmDMBPxydz27wLHx_ST_Poi3bYlRtgQxk7-y98NJksBsq7YkVD9ykuAdc_BY9j1LYGXsnYty2yh3f8AefP_Mp16oasw==',
            text = 'gAAAAABmmDMB7jWG6TiPYJtG3QYCg1O7jhKJEItwM19Kk46z6WDKRRUafvR6RUI1DlXK58U_E8qyErjw91thJObcPRBQrVvJtQvp2oddqku46OBpYXBTR4dNN7Jt5yYorNjSDkqSyC-2yXlcAl5ig5w8sws6ea-VCA==',
            secret = 'gAAAAABmmDMBYsvrT5BS-vWAkMKzT98MwcxuKgTPuWc2KPm-Ga3NZw4nkSAMmPuSMUcg-45ScemXdTtTieb_YvFw3a8DEeu6NQ==',
            destruction_date = timezone.now(),
            user = self.user
        )
        self.list_url = reverse("notes.list")
        self.new_url = reverse("notes.new")
        self.detail_url = reverse("notes.detail", args=[self.note1.secret])
        self.update_url = reverse("notes.update", args=[self.note1.secret])
        self.delete_url = reverse("notes.delete", args=[self.note2.secret])
    
    def test_get_notelist_view_loggedout(self):
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 302)
        
    def test_get_notedetail_view_loggedout(self):
        self.client.logout()
        response = self.client.get(self.detail_url)        
        self.assertEquals(response.status_code, 302)    
        
    def test_get_notenew_view_loggedout(self):
        self.client.logout()
        response = self.client.get(self.new_url)
        self.assertEquals(response.status_code, 302)
        
    def test_get_noteupdate_view_loggedout(self):
        self.client.logout()
        response = self.client.get(self.update_url)        
        self.assertEquals(response.status_code, 302) 
        
    def test_get_notedelete_view_loggedout(self):
        self.client.logout()
        response = self.client.get(self.delete_url)        
        self.assertEquals(response.status_code, 302) 
    
    def test_get_notelist_view_loggedin(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_list.html")
        
        
    def test_get_notedetail_view_loggedin(self):
        response = self.client.get(self.detail_url)        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_detail.html")
        
    def test_get_newnote_view_loggedin(self):
        response = self.client.get(self.new_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")
        
    def test_get_updatenote_view_loggedin(self):
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")
        
    def test_get_deletenote_view_loggedin(self):
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_delete.html")
        
    def test_post_notenew_view_loggedout(self):
        self.client.logout()
        response = self.client.post(self.new_url)
        self.assertEquals(response.status_code, 302)
        
    def test_post_noteupdate_view_loggedout(self):
        self.client.logout()
        response = self.client.post(self.update_url)        
        self.assertEquals(response.status_code, 302) 
        
    def test_post_notedelete_view_loggedout(self):
        self.client.logout()
        response = self.client.post(self.delete_url)        
        self.assertEquals(response.status_code, 302)   
        
        
    def test_post_newnote_view_loggedin(self):
        response = self.client.post(self.new_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")
        
    def test_post_updatenote_view_loggedin(self):
        response = self.client.post(self.update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")
        
