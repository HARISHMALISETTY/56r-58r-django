import json 
from django.http import HttpResponse,JsonResponse

class middleware1:
    def __init__(self,get_response):
        print("middleware1 is initiating")
        self.get_response=get_response
    def __call__(self,request):
        if request.path=="/home/":
            print("middleware1 is accepting requests for only home")
        response=self.get_response(request)
        return response


class middleware2:
    def __init__(self,get_response):
        print("middleware1 is initiating")
        self.get_response=get_response
    def __call__(self,request):
        if request.path=="/about/":
            print("middleware2 is accepting requests only for about")
        response=self.get_response(request)
        return response


class sscMiddleware:
    def __init__(self,get_response):        
        self.get_response=get_response
    def __call__(self,request):  
        if request.path=="/job1/" and request.method=="POST":
            incoming_data=json.loads(request.body) 
            ssc_status=incoming_data.get("ssc_status")     
            if ssc_status:
                response=self.get_response(request)
                return response
            return JsonResponse({"status":"failure","msg":"u should qualify ssc to apply for this job"})


class medicallyFitMiddleware:
    def __init__(self,get_response):        
        self.get_response=get_response
    def __call__(self,request):  
        if request.path=="/job1/" and request.method=="POST":
            incoming_data=json.loads(request.body) 
            medical_status=incoming_data.get("medically_fit")     
            if medical_status:
                response=self.get_response(request)
                return response
            return JsonResponse({"status":"failure","msg":"u should medically fit  to apply for this job"})

class ageValidationMiddleware:
    def __init__(self,get_response):        
        self.get_response=get_response
    def __call__(self,request):  
        if request.path=="/job1/" and request.method=="POST":
            incoming_data=json.loads(request.body) 
            age==incoming_data.get("age")     
            if age>21:
                response=self.get_response(request)
                return response
            return JsonResponse({"status":"failure","msg":"u should have atleast 21 years to apply for this job"})


#middleware we can use for many purposes 
# 1.validation
# 2.data encryption
#3.data formatting and cleaning

