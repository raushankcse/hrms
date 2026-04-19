from django.urls import path

from accounts.views import LoginApiView

urlpatterns= [
    path("login/", LoginApiView.as_view()),
]