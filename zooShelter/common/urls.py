from django.urls import path

from zooShelter.common import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home-page'),
    path('about/', views.AboutView.as_view(), name='about-page'),
    path('contact/', views.ContactView.as_view(), name='contact-page'),

]
