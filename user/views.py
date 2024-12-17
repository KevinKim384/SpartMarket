from django.shortcuts import render
from .forms import NewUserForm
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
    

# Create your views here.
def welcome_page(request):
    return render(request, 'user/welcome.html')

#--------------------------------------------------------
#로그인 및 새 계정 함수 모음
def login(request):
    if request.method == 'POST':
        id = request.GET.get('email')
        password = request.GET.get('password')
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = auth_login(request, username=id, password=password)
            if user is not None:
                login(request, user)
                return redirect('article:article')
    else:
        return redirect("/")

def signup(request):
    return 

#--------------------------------------------------------
#??