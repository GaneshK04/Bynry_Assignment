from django.contrib import admin
from django.urls import path, include
from service_requests.views import home, submit_request, request_success  # Import all views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service_requests/', include('service_requests.urls')),
    path('', home, name='home'),  # Home view for the root URL
]