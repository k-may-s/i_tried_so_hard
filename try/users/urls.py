from django.urls import path
from .views import create_client, read, details_client_view, delete_client, update_client_details

urlpatterns = [
    path('create/', create_client),
    path('', read),
    path('<int:id>/', details_client_view),
    path('delete/<int:id>/', delete_client),
    path('update/<int:id>/', update_client_details)
]
