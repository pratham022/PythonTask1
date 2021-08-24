from django.urls import path

from .views import home_page, add_post

urlpatterns = [
    path('', home_page, name='home'),
    path('create-new', add_post, name='create-new')
]