from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Accounts Home Page
    path('', views.accounts, name='accounts-home'),
]