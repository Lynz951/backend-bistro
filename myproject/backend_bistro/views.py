from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItems
from pprint import pprint
import json
import csv

# Create your views here.

def get_menu(request):
    data = [i.json() for i in MenuItems.objects.all()]
    return HttpResponse(json.dumps(data), content_type="application/json")

# def menu_by_category(request, letter):
#     return HttpResponse(f"Category letter is {letter}")

def menu_by_diet(request, dietid):
    data = [i.json() for i in MenuItems.objects.filter(diet_id = dietid)]
    if len(data) > 0:
        # Serialize obj to a JSON formatted str
        return HttpResponse(json.dumps(data), content_type="application/json") 
    else:
        return HttpResponse('No menu items have that diet id.')


def csv_database_write(request):

    # Get all data from UserDetail Databse Table
    data = [i.json() for i in MenuItems.objects.all()]

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'title', 'description', 'pirce', 'category id', 'diet id'])

    for item in data:
        writer.writerow([item.get('id'), item.get('title'), item.get('description'), item.get('price'), item.get('category_id'), item.get('diet_id')])

    return response
