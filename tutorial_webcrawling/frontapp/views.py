from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    html = "<u>Hello FrontApp</u>"
    
    return HttpResponse(html)

# template의 01_smaple.html 파일 호출
# 첫번째 값 : 요청으로 들어온 모든 값 넘기기
# 두번째 값 : 응답할 html파일명 정의
# 세번째 값 : html에 넣을 데이터들.. / 아무것도 안넣으면 사용안함
def sample(request):
    return render(request,
                    'frontapp/01_sample.html',
                    {})
def index(request):
    return render(request,
                    'frontapp/index.html',
                    {})
    
def blog(request):
    return render(request,
                    'frontapp/blog.html',
                    {})
def about_me(request):
    return render(request,
                    'frontapp/about_me.html',
                    {})
def index_css(request):
    return render(request,
                    'frontapp/index_css.html',
                    {})
    
def index_css2(request):
    return render(request,
                    'frontapp/index_css2.html',
                    {})
    
def index_css3(request):
    return render(request,
                    'frontapp/index_css3.html',
                    {})
    
def index_javascript1(request):
    return render(request,
                    'frontapp/index_javascript1.html',
                    {})
    
def index_javascript2(request):
    return render(request,
                    'frontapp/index_javascript2.html',
                    {})
def index_bootstrap1(request):
    return render(request,
                    'frontapp/index_bootstrap1.html',
                    {})

def login_form(request):
    return render(request,
                    'frontapp/form/01_form.html',
                    {})
    
def login_form_check(request):
    ### Get 방식으로 전달 받기
    if request.method == 'GET':
        mem_id = request.GET['mem_id']
        mem_pass = request.GET['mem_pass']
    ### Post 방식으로 전달 받기
    elif request.method == 'POST':
        mem_id = request.POST['mem_id']
        mem_pass = request.POST['mem_pass']
    
    return render(request,
                    'frontapp/form/02_form_check.html',
                    {"mem_id":mem_id,"mem_pass":mem_pass})