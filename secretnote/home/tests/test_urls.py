from django.test import SimpleTestCase
from django.urls import resolve, reverse
from home.views import LoginInterfaceView, HomeView, SignUpInterfaceView
from django.contrib.auth.views import LogoutView


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func.__name__, HomeView.as_view().__name__)

    def test_login_url_resolves(self):
        url = reverse("login")
        self.assertEquals(
            resolve(url).func.__name__, LoginInterfaceView.as_view().__name__
        )

    def test_logout_url_resolves(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func.__name__, LogoutView.as_view().__name__)

    def test_signup_url_resolves(self):
        url = reverse("signup")
        self.assertEquals(
            resolve(url).func.__name__, SignUpInterfaceView.as_view().__name__
        )
