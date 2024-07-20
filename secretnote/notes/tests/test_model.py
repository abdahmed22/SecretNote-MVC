import datetime
from django.test import TestCase
from notes.models import Note
from django.contrib.auth.models import User
from django.utils import timezone


class TestModel(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username="testuser", password="password")
        self.note1 = Note.objects.create(
            title="secret note 1",
            text="secret note 1 secret note 1 secret note 1 secret note 1",
            secret="secret",
            destruction_date=timezone.now(),
            user=self.user1,
        )
        self.note2 = Note.objects.create(
            title="gAAAAABmmDMBPxydz27wLHx_ST_Poi3bYlRtgQxk7-y98NJksBsq7YkVD9ykuAdc_BY9j1LYGXsnYty2yh3f8AefP_Mp16oasw==",
            text="gAAAAABmmDMB7jWG6TiPYJtG3QYCg1O7jhKJEItwM19Kk46z6WDKRRUafvR6RUI1DlXK58U_E8qyErjw91thJObcPRBQrVvJtQvp2oddqku46OBpYXBTR4dNN7Jt5yYorNjSDkqSyC-2yXlcAl5ig5w8sws6ea-VCA==",
            secret="gAAAAABmmDMBYsvrT5BS-vWAkMKzT98MwcxuKgTPuWc2KPm-Ga3NZw4nkSAMmPuSMUcg-45ScemXdTtTieb_YvFw3a8DEeu6NQ==",
            destruction_date=timezone.now() + datetime.timedelta(minutes=75),
            user=self.user1,
        )

    def test_note_is_assigned_created_date(self):
        self.assertEquals(self.note1.created.date(), timezone.now().date())
        self.assertEquals(self.note1.created.time().hour, timezone.now().time().hour)
        self.assertEquals(self.note1.created.time().min, timezone.now().time().min)
        self.assertEquals(
            self.note1.created.time().second, timezone.now().time().second
        )

    def test_note_is_assigned_to_user(self):
        self.assertEquals(self.note1, self.user1.notes.all()[0])

    def test_title_decryption(self):
        self.assertEquals(self.note1.title, self.note2.title_decrypted)

    def test_text_decryption(self):
        self.assertEquals(self.note1.text, self.note2.text_decrypted)

    def test_is_deleted(self):
        self.assertEquals(
            True, self.note1.is_deleted
        )  # since timezone.now() inside test file always behind timezone.now() inside model.

    def test_is_not_deleted(self):
        self.assertEquals(False, self.note2.is_deleted)
