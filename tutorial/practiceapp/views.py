from django.shortcuts import render
from django.http import HttpResponse
from .models import Lprod

# Create your views here.
def test(request):
    html = """
        <html>
        <head>
            <title>index</title>
        </head>
        <body>
            <u>테스트ㅡㅡㅡㅡㅡㅡ</u>
        </body>
        </html>
    """
    # 브라우저에 응답하기
    return HttpResponse(html)

def lprod_list(request):
    # lprod 전체 정보 갖고 오기
    lprod_list = Lprod.objects.all()
    
    return render(
            request,
            'practiceapp/lprod/lprod_list.html',
            {"lprod_list": lprod_list})
    
# 상세보기
def lprod_detail(request):
    
    if request.method == "GET":
        lprod_gu = request.GET["lprod_gu"]
        
    elif request.method == "POST":
        lprod_gu = request.POST["lprod_gu"]
        

    
    # lprod 상세 정보 1건 가지고 오기
    lprod_detail = Lprod.objects.get(lprod_gu=lprod_gu)
    return render(
        request,
        "practiceapp/lprod/lprod_detail.html",
        {"lprod_detail": lprod_detail}
    )