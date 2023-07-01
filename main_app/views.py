from django.shortcuts import render
from django.views import View # <- View class to handle request
from django.http import HttpResponse 

# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse("MoveScroll")