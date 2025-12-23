from django.shortcuts import render
from django.http import JsonResponse
from .models import OrderDetails,MovieBooking
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def GetOrders(request):
    try:
        if request.method=="GET":
            result=list(OrderDetails.objects.values()) #to get all the records from the table
            print(result)
            if len(result)==0:
                msg="No records found"
            else:
                msg="Data retrieved successfully"
            return JsonResponse({"status":"success","message":msg,"data":result,"total no.of records":len(result)})
        return JsonResponse({"status":"failure","message":"only get method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})

def BookingDetails(request):
    try:
        if request.method=="GET":
            result=list(MovieBooking.objects.values())

            if len(result)==0:
                msg="No records found"
            else:
                msg="Data retrieved successfully"            
            return JsonResponse({"status":"success","message":msg,"data":result,"total no.of records":len(result)})
        
        return JsonResponse({"status":"failure","message":"only get method allowed"})

    except Exception as e:
        return JsonResponse({"message":"something went wrong"})



@csrf_exempt
def orderPlacing(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            order=OrderDetails.objects.create(
                orderid=data["order_id"],
                useremail=data["email"],
                amount=data["amount"],
                status=data["status"],
                mode=data["mode"]
                )
            print(order.transaction_id)
            x=order.transaction_id
            return JsonResponse({
                "status":"success",
                "message":"payment details updated successfully",
                "transaction_id":x 
                },status=201)
        else:
            return JsonResponse({"error":"only post method is allowed"},status=400)
    except Exception as e:
        print(e)
        return JsonResponse({"error":"something went wrong"},status=500)

@csrf_exempt
def BookMyshow(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            MovieBooking.objects.create(moviename=data["movie_name"],
            showtime=data["show_time"],screenname=data["screen_name"])
            return JsonResponse({"status":"success","msg":"records inserted successfully"})
        return JsonResponse({"status":"failure","message":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})



student_info=[{"id":1,"name":"vasanth"},{"id":2,"name":"krishna"},{"id":3,"name":"kiran"}]

def getStudentById(request,id):
    filteredStudent=[]

    for student in student_info:
        if id==student["id"]:
            filteredStudent.append(student)

    return JsonResponse({"data":filteredStudent})

    




# {"order_id":"ord1","email":"harish123@gmail.com","amount":2500.50,"status":"success","mode":"paytm"}

# task:
# ------
# practise this
# create an api to book a movie ticket. with fields-->moviename,showtime,screenname,dateandtime,transcationid.