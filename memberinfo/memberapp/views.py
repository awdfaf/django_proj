from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
# Create your views here.
def mem_list(request):
    member_list = Member.objects.all()

    return render(
        request,
        'memberapp/member/mem_list.html',
        {"member_list":member_list}
    )

# 상세보기
def mem_detail(request):
    if request.method == "GET":
        mem_id = request.GET["mem_id"]
        
    elif request.method == "POST":
        mem_id = request.POST["mem_id"]
        

    # member 상세 정보 1건 가지고 오기
    mem_detail = Member.objects.get(mem_id=mem_id)
    return render(
        request,
        "memberapp/member/mem_detail.html",
        {"mem_detail": mem_detail}
    )
    
# 등록하기 / 등록 페이지 불러오기
def mem_insert(request):
    return render(
        request,
        "memberapp/member/mem_insert.html",
        {} 
    )


# 등록 데이터 저장
def mem_insert_save(request):
    if request.method == "GET" :
        mem_id     = request.GET["mem_id"]
        mem_pass   = request.GET["mem_pass"]
        mem_name = request.GET["mem_name"]
        mem_bir    = request.GET["mem_bir"]
        mem_add1    = request.GET["mem_add1"]
        mem_add2    = request.GET["mem_add2"]
        mem_hp    = request.GET["mem_hp"]
            
    elif request.method == "POST" :
        mem_id     = request.POST["mem_id"]
        mem_pass   = request.POST["mem_pass"]
        mem_name = request.POST["mem_name"]
        mem_bir    = request.POST["mem_bir"]
        mem_add1    = request.POST["mem_add1"]
        mem_add2    = request.POST["mem_add2"]
        mem_hp    = request.POST["mem_hp"]
    
    Member(mem_id=mem_id,
           mem_pass=mem_pass,
           mem_name=mem_name,
           mem_bir=mem_bir,
           mem_add1=mem_add1,
           mem_add2=mem_add2,
           mem_hp=mem_hp).save()
    url = "/member/list/"
    msg = """
            <script>
                alert('정상적으로 저장되었습니다.');
                location.href = '{}';
            </script>
        """.format(url)
    
    return HttpResponse(msg)


# 수정페이지
def mem_update(request):
    if request.method == "GET" :
        mem_id     = request.GET["mem_id"]
        
            
    elif request.method == "POST" :
        mem_id     = request.POST["mem_id"]
        
        
    
    mem_update = Member.objects.get(mem_id=mem_id)
    return render(
        request,
        "memberapp/member/mem_update.html",
        {"mem_update": mem_update}
    )
    
# 수정 적용
def mem_update_save(request):
    if request.method == "GET" :
        mem_id     = request.GET["mem_id"]
        mem_pass   = request.GET["mem_pass"]
        mem_name = request.GET["mem_name"]
        mem_bir    = request.GET["mem_bir"]
        mem_add1    = request.GET["mem_add1"]
        mem_add2    = request.GET["mem_add2"]
        mem_hp    = request.GET["mem_hp"]
            
    elif request.method == "POST" :
        mem_id     = request.POST["mem_id"]
        mem_pass   = request.POST["mem_pass"]
        mem_name = request.POST["mem_name"]
        mem_bir    = request.POST["mem_bir"]
        mem_add1    = request.POST["mem_add1"]
        mem_add2    = request.POST["mem_add2"]
        mem_hp    = request.POST["mem_hp"]
    
    Member.objects.filter(mem_id=mem_id).update(mem_pass=mem_pass,
                                                mem_name=mem_name,
                                                mem_bir=mem_bir,
                                                mem_add1=mem_add1,
                                                mem_add2=mem_add2,
                                                mem_hp=mem_hp)
    url = "/member/detail/"
    url = url + "?mem_id=" + mem_id 
    msg = """
            <script>
                alert('정상적으로 수정되었습니다.');
                location.href = '{}';
            </script>
        """.format(url)
    
    return HttpResponse(msg)