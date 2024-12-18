from django.shortcuts import render
from .forms import NewUserForm
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from .forms import CustumUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.
#--------------------------------------------------------
#이건 건들지마세요요
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, '로그인에 성공하였습니다! 환영합니다.')
            return redirect('articles:article')
    return render(request, 'user_html/login.html')
#--------------------------------------------------------
#로그인 및 새 계정 함수 모음

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = get_user_model()
        print(1)
        if not user.objects.filter(username=email).exists():
            print(2)
            user = user.objects.create_user(username=email, password=password)
            auth_login(request, user)
            messages.success(request, '회원가입에 성공하셨습니다! 환영합니다!')
            return redirect('/')
    print(3)
    return render(request, 'user_html/signup.html')

#--------------------------------------------------------
#??