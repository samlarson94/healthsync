from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Signup

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        signup = Signup.objects.create(email=email)
        signup.save()
    return render(request, 'signup.html')

