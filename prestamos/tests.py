from django.test import SimpleTestCase
from django.urls import reverse


class InicioViewTests(SimpleTestCase):
    def test_inicio_renders_page_using_base_template(self):
        response = self.client.get(reverse("inicio"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gestión de herramientas")
        self.assertContains(response, 'aria-label="Menú principal"')
