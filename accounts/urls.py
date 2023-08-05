from django.urls import path
from .views import login_view,signup_view,logout_user,verify_email,activate_user
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login/',login_view,name='login'),
    path('signup/',signup_view,name='signup'),
    path('logout/',logout_user,name='logout'),
    path('verify_email/',verify_email,name='verify_email'),
    path('activate/<uidb64>/<token>',activate_user,name='activate'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/sent_newpassword.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_done.html'),name='password_reset_complete'),
    
]