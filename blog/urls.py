from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_blog, name='create_blog'),
    path('update/<int:id>', update_blog, name='update_blog'),
    path('delete/<int:id>', delete_blog, name='delete_blog'),
]
