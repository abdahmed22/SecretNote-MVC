from django.test import TestCase
from notes.forms import NoteForm
from django.utils import timezone


class TestForm(TestCase):

    def setUp(self):
        self.testcases = [
            NoteForm(data={}),
            NoteForm(
                data={
                    "title": "only 1 form attribute",
                }
            ),
            NoteForm(
                data={
                    "title": "wrong date and time",
                    "text": "wrong date and time",
                    "secret": "wrong date and time",
                    "destruction_date": "wrong date and time",
                }
            ),
            NoteForm(
                data={
                    "title": "normal case",
                    "text": "normal case",
                    "secret": "normal case",
                    "destruction_date": timezone.now(),
                }
            ),
        ]

    def test_empty_form_is_not_valid(self):
        self.assertFalse(self.testcases[0].is_valid())
        self.assertEquals(len(self.testcases[0].errors), 4)

    def test_uncomplete_form_is_not_valid(self):
        self.assertFalse(self.testcases[1].is_valid())
        self.assertEquals(len(self.testcases[0].errors), 4)

    def test_wrong_data_form_is_not_valid(self):
        self.assertFalse(self.testcases[2].is_valid())
        self.assertEquals(len(self.testcases[0].errors), 4)

    def test_uncomplete_form_is_not_valid(self):
        self.assertTrue(self.testcases[3].is_valid())
