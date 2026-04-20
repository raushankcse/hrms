from django.urls import path

from accounts.views import LoginApiView, RefreshTokenView, LogoutApiView

urlpatterns= [
    path("login/", LoginApiView.as_view()),
    path("refresh/", RefreshTokenView.as_view()),
    path("logout/", LogoutApiView.as_view()),
]