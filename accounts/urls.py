from django.urls import path
from .views import login_view,signup_view,logout_user,verify_email,activate_user


urlpatterns=[
    path('login/',login_view,name='login'),
    path('signup/',signup_view,name='signup'),
    path('logout/',logout_user,name='logout'),
    path('verify_email/',verify_email,name='verify_email'),
    path('activate/<uidb64>/<token>',activate_user,name='activate')
]