from django.urls import path

from .views import home_page, add_post, login_page, register_page, logout_user

urlpatterns = [
    path('', home_page, name='home'),
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_page, name='register'),
    path('create-post', add_post, name='create-post'),
]