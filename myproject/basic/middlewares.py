import json 
from django.http import HttpResponse,JsonResponse
import re
from basic.models import User
from django.contrib.auth.hashers import make_password,check_password

# class middleware1:
#     def __init__(self,get_response):
#         print("middleware1 is initiating")
#         self.get_response=get_response
#     def __call__(self,request):
#         if request.path=="/home/":
#             print("middleware1 is accepting requests for only home")
#         response=self.get_response(request)
#         return response


# class middleware2:
#     def __init__(self,get_response):
#         print("middleware1 is initiating")
#         self.get_response=get_response
#     def __call__(self,request):
#         if request.path=="/about/":
#             print("middleware2 is accepting requests only for about")
#         response=self.get_response(request)
#         return response


# class sscMiddleware:
#     def __init__(self,get_response):        
#         self.get_response=get_response
#     def __call__(self,request):  
#         if request.path=="/job1/" and request.method=="POST":
#             incoming_data=json.loads(request.body) 
#             ssc_status=incoming_data.get("ssc_status")     
#             if ssc_status:
#                 response=self.get_response(request)
#                 return response
#             return JsonResponse({"status":"failure","msg":"u should qualify ssc to apply for this job"})


# class medicallyFitMiddleware:
#     def __init__(self,get_response):        
#         self.get_response=get_response
#     def __call__(self,request):  
#         if request.path=="/job1/" and request.method=="POST":
#             incoming_data=json.loads(request.body) 
#             medical_status=incoming_data.get("medically_fit")     
#             if medical_status:
#                 response=self.get_response(request)
#                 return response
#             return JsonResponse({"status":"failure","msg":"u should medically fit  to apply for this job"})

# class ageValidationMiddleware:
#     def __init__(self,get_response):        
#         self.get_response=get_response
#     def __call__(self,request):  
#         if request.path=="/job1/" and request.method=="POST":
#             incoming_data=json.loads(request.body) 
#             age==incoming_data.get("age")     
#             if age>21:
#                 response=self.get_response(request)
#                 return response
#             return JsonResponse({"status":"failure","msg":"u should have atleast 21 years to apply for this job"})

class authMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        self.username_pattern = re.compile(r'^[a-zA-Z0-9_]{5,15}$')
        self.password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#]{8,}$')
        self.email_pattern = re.compile(r'^[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}$')
    def __call__(self,request):
        if request.path in ["/signup/", "/login/"] and request.method == "POST":
             try:
                data = json.loads(request.body)
             except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON data"}, status=400)
             if request.path == "/signup/":
                username = data.get("username")
                email = data.get("email")
                password = data.get("password")
                if not all([username, email, password]):
                    return JsonResponse({"error": "All fields are required"}, status=400)

                if not self.username_pattern.match(username):
                    return JsonResponse({"error": "Invalid username format"}, status=400)

                if not self.email_pattern.match(email):
                    return JsonResponse({"error": "Invalid email format"}, status=400)

                if not self.password_pattern.match(password):
                    return JsonResponse({"error": "Weak password"}, status=400)

                if User.objects.filter(username=username).exists():
                    return JsonResponse({"error": "Username already exists"}, status=400)

                if User.objects.filter(email=email).exists():
                    return JsonResponse({"error": "Email already exists"}, status=400)
 
             if request.path == "/login/":
                username = data.get("username")
                password = data.get("password")
                print(password)

                if not all([username, password]):
                    return JsonResponse({"error": "Username & password required"}, status=400)

                try:
                    user = User.objects.get(username=username)
                    print(user)
                except User.DoesNotExist:
                    return JsonResponse({"error": "Invalid username"}, status=401)

                # if user.password != password:
                if not check_password(password,user.password):
                    return JsonResponse({"error": "Invalid password"}, status=401)

        response=self.get_response(request)
        return response
