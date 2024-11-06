# FILE: Authentication/urls.py

from django.urls import path, re_path
from .views import RegisterView, ActivateAccountView, LoginView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    re_path(r'^activate/(?P<uidb64>[^/]+)/(?P<token>.+)/$', ActivateAccountView.as_view(), name='activate'),
    path('login/', LoginView.as_view(), name='login'),
]