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