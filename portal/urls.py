from django.urls import path
from .views import *

urlpatterns = [
    path('',welcome_page, name='welcome_page'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('privacy/', privacy, name='privacy'),
    path('QnA/', qna, name='qna'),
    path('addQnA/', addqna, name='addqna'),
    path('tAndC/', terms, name='terms'),
]
