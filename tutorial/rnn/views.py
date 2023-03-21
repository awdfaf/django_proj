from django.shortcuts import render
from django.http import HttpResponse
from rnn.model import rnn as cl
# Create your views here.

def viewpage(request):
    
    return render(request,
                "rnn/generator.html",
                {}
    )
def load(request):
    if request.method == "GET":
        current_word = request.GET["current_word"]
        n = request.GET["n"]
    elif request.method == "POST":
        current_word = request.POST["current_word"]
        n = request.POST["n"]
    ld = cl.Load_rnn()
    current_word = str(current_word)
    n = int(n)
    sentence = ld.sentence_generator(current_word=current_word,n=n)
    
    return render(request,
                "rnn/generator.html",
                {"sentence":sentence })
    
                