from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    return render(request, 'home.html')

def my_logout(request):
    my_logout(request)
    return redirect('home')

