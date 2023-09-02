from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "pages/about.html"


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)
