from django.urls import path

from accounts.views import LoginApiView, RefreshTokenView, LogoutApiView, UserListView, AdminSetPasswordView

urlpatterns= [
    path("login/", LoginApiView.as_view()),
    path("refresh/", RefreshTokenView.as_view()),
    path("logout/", LogoutApiView.as_view()),
    path("users/", UserListView.as_view()),
    path("admin/set-password/", AdminSetPasswordView.as_view()),
]