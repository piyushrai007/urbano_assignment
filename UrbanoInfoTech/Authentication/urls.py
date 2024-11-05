# accounts/urls.py
from django.urls import path
from .views import RegisterView, ActivateAccountView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('activate/<uid>/<token>/', ActivateAccountView.as_view(), name='activate'),
]
