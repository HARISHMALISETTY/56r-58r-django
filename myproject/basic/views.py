from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math 
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import userProfile,Employee,User
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password,check_password
import jwt
from datetime import datetime, timedelta
from django.conf import settings

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


# response={"status":"success","pagenum":2,"limit":4,"total_pages":4,"data":[{},{},{}]}

def pagination(request):
    data=['apple','banana','carrot','grapes','watermelon','kiwi','pineapple','custard-apple','strawberry','blueberry','dragonfruit']
    page=int(request.GET.get("page",1))
    limit=int(request.GET.get("limit",3))

    start=(page-1)*limit
    end=page*limit
    total_pages=math.ceil(len(data)/limit)
    result=data[start:end]

    res={"status":"success","current_page":page,"total_pages":total_pages,"data":result}
    return JsonResponse(res,status=302)

@csrf_exempt
def createData(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body) #dictionary
            name=data.get("name") #taking name property from dict
            age=data.get("age") #taking age property from dict
            city=data.get("city") #taking city property from dict
            userProfile.objects.create(name=name,age=age,city=city)
            print(data)
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    except Exception as e:
        return JsonResponse({"statuscode":500,"message":"internal server error"})

@csrf_exempt
def createProduct(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
    return JsonResponse({"status":"success","data":data,"statuscode":201})
@csrf_exempt
def createEmployee(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            print(data)
            Employee.objects.create(emp_name=data.get("name"),emp_salary=data.get("sal"),emp_email=data.get("email"))
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    except IntegrityError as e:        
        return JsonResponse({"status":"error","message":"inputs are invalid or not acceptable"},status=400)
    finally:
        print("done")

@csrf_exempt       
def UpdateUserCityById(request):
    try:
        if request.method=="PUT":
            input_data=json.loads(request.body)
            ref_id=input_data["id"]
            new_city=input_data["new_city"]
            update=userProfile.objects.filter(id=ref_id).update(city=new_city)
            if update==0:
                msg="no record found"
            else:
                msg="record updated"
            print(update)
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure",":msg":"only put method is allowed"},status=400)
    except Exception as e:
         return JsonResponse({"status":"error","message":"something went wrong"},status=500)


@csrf_exempt
def updateUseragebyId(request):
    try:
        if request.method=="PUT":
            input_data=json.loads(request.body)
            ref_id=input_data["id"]
            new_age=input_data["new_age"]
            update=userProfile.objects.filter(id=ref_id).update(age=new_age)
            if update==0:
                msg="no record found with referrence of id"
            else:
                msg="record is updated successfully"
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure",":msg":"only put method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","message":"something went wrong"},status=500)
@csrf_exempt
def DeleteUserById(request,ref_id):
    try:
        if request.method=="DELETE": 
            delete=userProfile.objects.filter(id=ref_id).delete() 
            print(delete[0])  
            if delete[0]==0:
                msg="no record is found to delete"
            else:
                msg="record is deleted successfully"        
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure",":msg":"only DELETE method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","message":"something went wrong"},status=500)


@csrf_exempt
def job1(request):
    try:
        if request.method=="POST":
            
            return JsonResponse({"status":"success","message":"job1 applied successfully"})
        return JsonResponse({"status":"failure","message":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"status":"error","message":"something went wrong"},status=500)


@csrf_exempt
def job2(request):
    try:
        if request.method=="POST":
            return JsonResponse({"status":"success","message":"job2 applied successfully"})
        return JsonResponse({"status":"failure","message":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"status":"error","message":"something went wrong"},status=500)

@csrf_exempt
def signup(request):
    data = json.loads(request.body)
    hashed_password=make_password(data["password"])
    user = User.objects.create(
        username=data["username"],
        email=data["email"],
        password=hashed_password,
        role=data["role"]
    )

    return JsonResponse({
        "status": "success",
        "msg": "User registered successfully"
    }, status=201)

@csrf_exempt
def login(request):
    user_info=json.loads(request.body)
    username=user_info.get("username")
    user_existing_info=list(User.objects.filter(username=username).values())
    print(user_existing_info)
    
    payload={
        "username":username,
        "iat": datetime.utcnow(),
        "role":user_existing_info[0].get("role"),
        "exp": datetime.utcnow() + timedelta(seconds=settings.JWT_EXP_TIME)}

    token=jwt.encode(payload,settings.JWT_SECRET_KEY,algorithm=settings.JWT_ALGORITHM)

    return JsonResponse({

        "status": "success",
        "msg": "Login successful",
        "greetings":f"welcome {username}",
        "token":token
    })
@csrf_exempt
def protected_api(request):
    try:
        if request.method=="POST":
            auth_header = request.headers.get("Authorization")
            token=auth_header.split(" ")[1]
            print(token[1]) #readig token from input
            if not auth_header:
                return JsonResponse(
                    {"msg": "Authorization header missing"},
                    status=401
                )
            try:
                # print(auth_header)
                decoded_payload = jwt.decode(
                                    token,
                                    settings.JWT_SECRET_KEY,
                                    algorithms=[settings.JWT_ALGORITHM]
                                    )
                print(decoded_payload)
                if decoded_payload.get("role")=="admin":
                    return JsonResponse({"msg":"u have access for this api"})
                else:
                    return JsonResponse({"msg":"u have not access for this api"},status=401) 
                return JsonResponse({"msg":"successfully token recieved"})
            except Exception as e:
                return JsonResponse({"msg":"something went wrong","error":e})
        return JsonResponse({"msg":"done"})
    except:
        return JsonResponse({"msg":"only post method allowed"})












