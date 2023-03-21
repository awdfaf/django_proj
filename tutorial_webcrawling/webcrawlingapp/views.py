from django.shortcuts import render
from django.http import HttpResponse
from webcrawlingapp.web.webcrawling import WebCrawing
from .models import Melon
# Create your views here.

# 웹 크롤링 결과 db에 저장 하기
def webCrawling(request):
    # 클래스 생성
    wc = WebCrawing("http://www.melon.com/chart/index.htm")
    # 웹크롤링 데이터 조회
    model_list = wc.getData()
    #웹드라이버 종료
    wc.webdriver_quit()

    # db에 저장 하기
    # melon 테이블에는 10개의 데이터만 유지
    # 데이터가 없으면 insert, 있으면 update
    melon_cnt = Melon.objects.all().count()
    if melon_cnt > 0:
        # 데이터가 있으면 수정
        for data in model_list:
            Melon.objects.filter(no = data["no"]).update(no=data["no"],
                  title=data["title"],
                  singer=data["singer"])
    else:
        # 데이터가 없으면 입력
        for data in model_list:
            Melon(no=data["no"],
                  title=data["title"],
                  singer=data["singer"]).save()
    
    # return render(request,
    #             'webcrawlingapp/webcrawling.html',
    #             {"melon_list": model_list})
    msg = """
        <script>
            alert("웹크롤링 및 DB 입력/수정 성공쓰");
            location.href = '/crawling/';
            </script>
    """
    return HttpResponse(msg)

    
    
    
    
# 멜론 top10 조회
def melonList(request):
    melon_list = Melon.objects.all()
    return render(request,
                    "webcrawlingapp/webcrawling.html",
                    {"melon_list": melon_list})
