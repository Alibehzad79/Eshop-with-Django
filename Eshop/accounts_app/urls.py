from django.urls import path
from accounts_app.views import SignUpView, dashboard, edit_account_details
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, LoginView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView

urlpatterns = [
    path("accounts/register/", SignUpView.as_view(), name="register"),
    path("accounts/login/", LoginView.as_view(template_name='accounts/registration/login.html'), name='login'),
    path("accounts/logout/", LogoutView.as_view(), name='logout'),
    path('accounts/dashboard/', dashboard, name="dashboard"),
    path('accounts/dashboard/edit-account-detail/', edit_account_details, name="edit-account-detail"),
    path("accounts/password_change/",
         PasswordChangeView.as_view(template_name='accounts/registration/password_change.html'),
         name='password_change'),
    path("accounts/password_change/done/",
         PasswordChangeDoneView.as_view(template_name='accounts/registration/password_change_done.html'),
         name='password_change_done'),
    path("accounts/password_reset/",
         PasswordResetView.as_view(template_name="accounts/registration/password_reset.html"), name='password_reset'),
    path("accounts/password_reset_done/",
         PasswordResetDoneView.as_view(template_name="accounts/registration/password_reset_done.html"),
         name='password_reset_done'),

    path("accounts/reset/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(template_name="accounts/registration/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path("accounts/reset/done/",
         PasswordResetCompleteView.as_view(template_name="accounts/registration/password_reset_complete.html"),
         name='password_reset_complete'),
]
