from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Hello 문구를 브라우저에 보이기 위한 html 생성하기
def index(request):
    html = """
        <html>
        <head>
            <title>index</title>
        </head>
        <body>
            <u>index 페이지 입니다.</u>
        </body>
        </html>
    """
    # 브라우저에 응답하기
    return HttpResponse(html)
def root(request):
    html = """
        <html>
        <head>
            <title>index</title>
        </head>
        <body>
            <u>index 페이지 입니다.</u>
        </body>
        </html>
    """
    # 브라우저에 응답하기
    return HttpResponse(html)
    
def index1(request):
    # 브라우저에 응답하기
    return HttpResponse("<u>hi</u>")    
    
def index2(request):
    # 브라우저에 응답하기
    return HttpResponse("<u>Main</u>")        
    
    
def index3(request):
    return HttpResponse("<u>awdfaf</u>")    