from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
arr=['Python','Perl','java','javascript','C','C++','SQL','SWIFT','Django','PHP','objectiv-C','ruby','VirtualBasic','R']
globalcnt = dict()
def index(request):

    mydictionary={
        'arr':arr
    }
    return render(request,'index.html',context=mydictionary)
def getquery(request):
    q=request.GET['languages']
    if q in globalcnt:
        #if already exist then increment the value
        globalcnt[q] = globalcnt[q]+1
    else:
        #first occurence
        globalcnt[q]=1
    mydictionary={
        'arr':arr,
        'globalcnt':globalcnt

    }
    return render(request,'index.html',context=mydictionary)
def sortdata(request):
    global globalcnt
    globalcnt=dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True ))

    mydictionary = {
        'arr': arr,
        'globalcnt':globalcnt
    }
    return render(request, 'index.html', context=mydictionary)
