from django.urls import path,re_path
from .views import homepage,service_worker,manifest


urlpatterns=[
    path('',homepage,name='home'),
    re_path(r'^serviceworker\.js$', service_worker, name='serviceworker'),
    re_path(r'^manifest\.json$', manifest, name='manifest'),
    
]