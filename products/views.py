from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at product api")

def ProductView(APIView):
    def post(self, request):
        pass

    def get(self, request):
        pass