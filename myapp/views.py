from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def todos(request):
    return render(request,"todos.html")

def tests(request):
    return render(request,"tests.html")

def about(request):
    return render(request,"about.html")


def print_message(request):
    return "test123"
def get_today_date():
    from datetime import datetime 
    return str(datetime.now)