from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import path

import authentication.views
import tournaments.views
import teams.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        LoginView.as_view(
            template_name="authentication/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="authentication/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "change-password-done/",
        PasswordChangeDoneView.as_view(
            template_name="authentication/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path("signup/", authentication.views.signup_page, name="signup"),
    path("home/", authentication.views.home, name="home"),
    path("rules/", tournaments.views.rules, name="rules"),
    path("teams/", teams.views.teams, name="teams"),
    path("calendar/", tournaments.views.calendar, name="calendar"),
]
