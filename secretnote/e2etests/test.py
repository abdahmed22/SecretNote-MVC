from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestNavBar(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_secretnote(self):
        self.browser.get(self.live_server_url)

        navbar = self.browser.find_element(By.ID, "navbar")
        navbar.find_element(By.ID, "signup_button").click()

        signup_form = self.browser.find_element(By.ID, "signup_form")
        signup_form.find_element(By.ID, "id_username").send_keys("username")
        signup_form.find_element(By.ID, "id_password1").send_keys("strongPassword11")
        signup_form.find_element(By.ID, "id_password2").send_keys("strongPassword11")
        signup_form.find_element(By.ID, "signup_submit").click()

        navbar = self.browser.find_element(By.ID, "navbar")
        navbar.find_element(By.ID, "login_button").click()

        login_form = self.browser.find_element(By.ID, "login_form")
        login_form.find_element(By.ID, "id_username").send_keys("username")
        login_form.find_element(By.ID, "id_password").send_keys("strongPassword11")
        login_form.find_element(By.ID, "login_submit").click()

        home = self.browser.find_element(By.ID, "home")
        home.find_element(By.ID, "create_button").click()

        note_form = self.browser.find_element(By.ID, "note_form")
        note_form.find_element(By.ID, "id_title").send_keys("secret note")
        note_form.find_element(By.ID, "id_text").send_keys(
            "secret note secret note secret note secret note"
        )
        note_form.find_element(By.ID, "id_secret").send_keys("secret")
        note_form.find_element(By.ID, "id_destruction_date").send_keys("222225666")
        note_form.find_element(By.ID, "note_submit").click()

        note_list = self.browser.find_element(By.ID, "note_list")
        note_list.find_element(By.ID, "view_button").click()

        note_detail = self.browser.find_element(By.ID, "note_detail")
        self.assertEquals(note_detail.find_element(By.ID, "title").text, "secret note")
        self.assertEquals(
            note_detail.find_element(By.ID, "text").text,
            "secret note secret note secret note secret note",
        )
