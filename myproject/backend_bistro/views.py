from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItems
from pprint import pprint
# Create your views here.

def get_menu(request):
    menu = list(MenuItems.objects.values())
    return JsonResponse({'data': menu})

# def menu_by_category(request, letter):

#     return HttpResponse(f"Category letter is {letter}")

def menu_by_diet(request, dietid):
    menu = list(MenuItems.objects.filter(diet_id=dietid).values())
    # return HttpResponse(f"Diet id is {dietid}")
    if len(menu) > 0:
        return JsonResponse({'data': menu})
    else:
        return HttpResponse('No menu items have that diet id.')