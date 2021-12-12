from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.list, name="list"),
    path('create', views.create, name="create"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
    path('register', views.register, name="register"),
    path('login', views.log_in, name="login"),
    path('logout', views.log_out, name="logout"),
    ]