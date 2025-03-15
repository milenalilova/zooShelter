from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zooShelter.common.urls')),
    path('accounts/', include('zooShelter.accounts.urls')),
    path('animals/', include('zooShelter.animals.urls')),

]
