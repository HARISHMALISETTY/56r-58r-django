from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def sample(request):
    print(request)
    qp1=request.GET.get("name")
    qp2=request.GET.get("city")
    return HttpResponse(f"{qp1} is from {qp2}")

def sample1(request):
    info={"data":[{"name":"akanksha","city":"hyd","gender":"female"},{"name":"uma","city":"bnglr","gender":"female"},{"name":"durgaprasad","city":"vij","gender":"male"}]}
    return JsonResponse(info)
