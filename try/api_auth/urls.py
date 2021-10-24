from django.urls import path
from .views import AuthView

urlpatterns = [
    path('create_user/', AuthView.create_user, name='create'),
    path('authenticate/basic', AuthView.authenticate_user, name='authenticate')
]
