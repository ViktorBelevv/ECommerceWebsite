from django.urls import path

from ecom.accounts.views import login_user, register_user, logout_user

urlpatterns = [
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    path('logout/', logout_user, name='logout user'),
]