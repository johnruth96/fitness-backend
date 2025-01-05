from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('v1/', include('fitness.urls', namespace='fitness')),
]
