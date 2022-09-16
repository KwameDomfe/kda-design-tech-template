# Imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    path, include
    )

# core urls
urlpatterns = [

    path('admin/', admin.site.urls),
    #1. Website
    path('', include('apps.website.urls')),
    #2. Accounts
    path('accounts/', include('apps.accounts.urls')),
    
] + static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
    ) + static(
    settings.STATIC_URL, document_root = settings.STATIC_ROOT)
