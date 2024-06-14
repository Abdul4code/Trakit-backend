from django.contrib import admin
from django.urls import path, include


from users.views import Register, Login, Logout, UpdatePassword

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('forgot/', UpdatePassword.as_view()),
]
