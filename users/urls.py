from django.urls import path
from .views import home, profile, RegisterView
from . import views

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('Users/mubu/mizbee.zip', views.download_file, name='mizbee'),
    path('download/', views.download, name ='download'),
]
