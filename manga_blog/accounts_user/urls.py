from django.urls import path

from django.contrib.auth import views as auth_views

from .import views

urlpatterns = [
  # path('',views.accueil,name='accueil'),
  path('',views.home,name='home'),

  # Urls accounts resgister user
  path('login/',views.login_view,name='login'),

  path('register/',views.register_view,name='register'),

  path('logout/',views.logout_view,name='logout'),

  path('profil_user/',views.profil_user,name='profile_user'),

  path('change_info_user/',views.change_info_user,name="change_info"),

  path('change_password/',views.change_password,name="change_password"),

  path('change_profile_image/',views.change_profile_image, name="change_image_profil"),

  # URls accounts reset password user
  path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),

  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),

  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),

  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),

]
