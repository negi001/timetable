from django.shortcuts import render

# Create your views here.

# dashboard
def index(request):
    return render(request,'dashboard.html')

def _login(request):
    return render(request, 'login.html')