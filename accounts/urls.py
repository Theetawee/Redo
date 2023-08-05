from django.urls import path
from .views import login_view,signup_view,logout_user


urlpatterns=[
    path('login/',login_view,name='login'),
    path('signup/',signup_view,name='signup'),
    path('logout/',logout_user,name='logout')
]