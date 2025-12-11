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

#dynamic response using query params
def productInfo(request):
    product_name=request.GET.get("product",'mobile')
    quantity=int(request.GET.get("quantity",1))
    price=int(request.GET.get("price",25000))
    data={"product":product_name,"quantity":quantity,"price":price,"totalprice":price*quantity}
    return JsonResponse(data)

#filtering using query params

def filteringData(request):
    data=[1,2,3,4,5,6,7,8,9,10]
    filteredData=[]

    qp=int(request.GET.get("num",2))

    for x in data:
        if x%qp==0:
            filteredData.append(x)

    return JsonResponse({"data":filteredData})

students_data=[{'name':'durgaprasad','city':'hyd'},{'name':'rajendra','city':'hyd'},{'name':'uma','city':'bnglr'},{'name':'kiran','city':'bnglr'}]

def filterStudentsByCity(request):
    filteredStudents=[]
    city=request.GET.get("city","hyd")

    for student in students_data:
        if student["city"]==city:
            filteredStudents.append(student)
    return JsonResponse({"status":"success","data":filteredStudents})


response={"status":"success","pagenum":2,"limit":4,"total_pages":4,"data":[{},{},{}]}

