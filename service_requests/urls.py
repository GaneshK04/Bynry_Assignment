from django.urls import path
from .views import submit_request, request_success

urlpatterns = [
    path('submit/', submit_request, name='submit_request'),
    path('success/', request_success, name='request_success'),
]