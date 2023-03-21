from django.shortcuts import render
from django.http import HttpResponse
from .models import Prod
# Create your views here.
def prod_list(request):
    prod_list = Prod.objects.all()

    return render(
        request,
        'parkgw_app/prod/prod_list.html',
        {"prod_list":prod_list}
    )
    
def prod_detail(request):
    if request.method == "GET":
        prod_id = request.GET["prod_id"]
        
    elif request.method == "POST":
        prod_id = request.POST["prod_id"]
        

    # member 상세 정보 1건 가지고 오기
    prod_detail = Prod.objects.get(prod_id=prod_id)
    return render(
        request,
        "parkgw_app/prod/prod_detail.html",
        {"prod_detail": prod_detail}
    )
    
# sns 로그인 화면 생성
def login_logout(request):
    prod_list = Prod.objects.all()
    return render(
        request,
        "parkgw_app/prod/prod_list.html",
        {"prod_list":prod_list}
    )
    
    
    
def prod_update(request):
    if request.method == "GET" :
        prod_id     = request.GET["prod_id"]
        
            
    elif request.method == "POST" :
        prod_id     = request.POST["prod_id"]
        
        
    
    prod_update = Prod.objects.get(prod_id=prod_id)
    return render(
        request,
        "parkgw_app/prod/prod_update.html",
        {"prod_update": prod_update}
    )
    
def prod_update_save(request):
    if request.method == "GET" :
        prod_id     = request.GET["prod_id"]
        prod_name     = request.GET["prod_name"]
        prod_lgu     = request.GET["prod_lgu"]
        prod_buyer     = request.GET["prod_buyer"]
        prod_sale     = request.GET["prod_sale"]     
        
    elif request.method == "POST" :
        prod_id     = request.POST["prod_id"]
        prod_name     = request.POST["prod_name"]
        prod_lgu     = request.POST["prod_lgu"]
        prod_buyer     = request.POST["prod_buyer"]
        prod_sale     = request.POST["prod_sale"]     
    
    Prod.objects.filter(prod_id=prod_id).update(prod_name = prod_name,prod_lgu=prod_lgu,prod_buyer=prod_buyer,prod_sale=prod_sale)
        
    url = "/prod/detail/"
    url = url + "?prod_id=" + prod_id 
    msg = """
            <script>
                alert('정상적으로 수정되었습니다.');
                location.href = '{}';
            </script>
        """.format(url)
    
    return HttpResponse(msg)

def prod_insert(request):
    return render(
        request,
        "parkgw_app/prod/prod_insert.html",
        {} 
    )
def prod_insert_save(request):
    if request.method == "GET" :
        prod_id     = request.GET["prod_id"]
        prod_name     = request.GET["prod_name"]
        prod_lgu     = request.GET["prod_lgu"]
        prod_buyer     = request.GET["prod_buyer"]
        prod_sale     = request.GET["prod_sale"]     
        
    elif request.method == "POST" :
        prod_id     = request.POST["prod_id"]
        prod_name     = request.POST["prod_name"]
        prod_lgu     = request.POST["prod_lgu"]
        prod_buyer     = request.POST["prod_buyer"]
        prod_sale     = request.POST["prod_sale"]    
    
    Prod(prod_id=prod_id,
        prod_name=prod_name,
        prod_lgu=prod_lgu,
        prod_buyer=prod_buyer,
        prod_sale=prod_sale,
        prod_cost=0,
        prod_price=0,
        prod_outline="null",
        prod_img="null",
        prod_totalstock=0,
        prod_properstock=0).save()
    
    url = "/prod/list/"
    msg = """
            <script>
                alert('정상적으로 저장되었습니다.');
                location.href = '{}';
            </script>
        """.format(url)
    
    return HttpResponse(msg)