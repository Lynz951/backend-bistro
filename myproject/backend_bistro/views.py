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
    data = list(MenuItems.objects.filter(diet_id=dietid).values())
    # return HttpResponse(f"Diet id is {dietid}")
    if len(menu) > 0:
        return JsonResponse({data})
    else:
        return HttpResponse('No menu items have that diet id.')