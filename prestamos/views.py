from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import TemplateView


@login_required
def inicio(request):
    return render(request, "prestamos/inicio.html")


class PanelEncargadoView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "prestamos/panel_encargado.html"

    def test_func(self):
        return self.request.user.is_staff
