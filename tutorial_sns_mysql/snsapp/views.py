from django.shortcuts import render

# Create your views here.
# sns 로그인 화면 생성
def login_logout(request):
    return render(
        request,
        "snsapp/login.html",
    )
