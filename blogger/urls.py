from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home_page, name = 'home_page'),

    path('login/',blogger_login, name='blogger_login'),
    path('logout/', blogger_logout, name='blogger_logout'),

    path('signup/', blogger_signup, name='blogger_signup'),
    path('profile/', blogger_profile, name='blogger_profile'),
    path('profile_update/', profile_update, name='profile_update'),

    path('update_password/', update_password, name='update_password'),
]
