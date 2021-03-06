# from django.conf.urls import url
from django.urls import path
from basic_app import views

# Template urls
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.registration, name='register'),
    path('user_login/', views.user_login, name='user_login')
]
