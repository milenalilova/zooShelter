from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'common/home-page.html'


class AboutView(TemplateView):
    template_name = 'common/about-page.html'
