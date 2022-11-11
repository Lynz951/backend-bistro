from django.urls import path

from . import views

urlpatterns = [
    path('backend_bistro/', views.get_menu),
    path('backend_bistro/<int:dietid>/', views.menu_by_diet),
    path('export/csv-database-write/', views.csv_database_write, name='csv_database_write'),
    
    # path('backend_bistro/<str:letter>/', views.menu_by_category),
    
]