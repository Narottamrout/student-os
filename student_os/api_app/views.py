# from django.http import JsonResponse

# def hello(request):
#     return JsonResponse({
#         "message": "Student OS Backend Running Successfully 🚀"
#     })
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to Student OS 🚀"
    })

def hello(request):
    return JsonResponse({
        "message": "Student OS Backend Running Successfully 🚀"
    })