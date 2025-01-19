from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

def submit_request(request):
    """
    Handles the submission of service requests.
    If the request method is POST, it processes the form data.
    If the form is valid, it saves the data and redirects to the success page.
    Otherwise, it displays the empty form.
    """
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('request_success')  # Redirect to the success page
    else:
        form = ServiceRequestForm()  # Create an empty form instance
    return render(request, 'service_requests/submit_request.html', {'form': form})

def request_success(request):
    """
    Displays a success message after a service request is submitted.
    """
    return render(request, 'service_requests/request_success.html')

def home(request):
    """
    Displays the home page with a welcome message and a link to submit a service request.
    """
    return render(request, 'service_requests/home.html')