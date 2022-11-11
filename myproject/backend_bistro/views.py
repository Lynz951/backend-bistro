from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItems
from pprint import pprint
import json

# Create your views here.

def get_menu(request):
    data = [i.json() for i in MenuItems.objects.all()]
    return HttpResponse(json.dumps(data), content_type="application/json")

# def menu_by_category(request, letter):
#     return HttpResponse(f"Category letter is {letter}")

def menu_by_diet(request, dietid):
    data = [i.json() for i in MenuItems.objects.filter(diet_id = dietid)]
    if len(data) > 0:
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return HttpResponse('No menu items have that diet id.')
