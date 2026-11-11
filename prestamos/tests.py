from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AuthenticationViewTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.member = user_model.objects.create_user(
            username="socio",
            password="test-password",
        )
        self.staff = user_model.objects.create_user(
            username="encargado",
            password="test-password",
            is_staff=True,
        )

    def test_home_requires_login_and_renders_for_authenticated_user(self):
        response = self.client.get(reverse("inicio"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('inicio')}",
        )

        self.client.force_login(self.member)
        response = self.client.get(reverse("inicio"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gestión de herramientas")
        self.assertContains(response, "Conectado: socio")
        self.assertContains(response, "Cerrar sesión")

    def test_staff_panel_is_for_staff_only(self):
        self.client.force_login(self.member)
        self.assertEqual(
            self.client.get(reverse("panel_encargado")).status_code,
            403,
        )

        self.client.force_login(self.staff)
        self.assertEqual(
            self.client.get(reverse("panel_encargado")).status_code,
            200,
        )

    def test_login_and_post_logout(self):
        response = self.client.post(
            reverse("login"),
            {"username": "socio", "password": "test-password"},
        )
        self.assertRedirects(response, reverse("inicio"))

        response = self.client.post(reverse("logout"))
        self.assertRedirects(response, reverse("login"))
