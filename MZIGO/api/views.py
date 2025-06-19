from django.http import JsonResponse
from django.views import View

class ExampleView(View):
    def get(self, request):
        data = {
            "message": "Hello, this is a sample endpoint!"
        }
        return JsonResponse(data)

    def post(self, request):
        # Here you would handle POST requests
        data = {
            "message": "This is a POST request!"
        }
        return JsonResponse(data)