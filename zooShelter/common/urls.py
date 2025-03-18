from django.urls import path

from zooShelter.common import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home-page'),

]
