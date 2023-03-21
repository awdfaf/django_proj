from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request):
    html = """
        <html>
        <head>
            <title>index</title>
        </head>
        <body>
            <u>aaaa</u>
        </body>
        </html>
    """
    # 브라우저에 응답하기
    return HttpResponse(html)

def sample(request):
    return render(request,
                    'secondapp/02_sample.html',
                    {})