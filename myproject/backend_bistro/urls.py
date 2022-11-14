from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'menuitems', views.MenuItemsViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('backend_bistro/', views.get_menu),
    path('backend_bistro/<int:dietid>/', views.menu_by_diet),
    # path('export/csv-database-write/', views.csv_database_write, name='csv_database_write'),
    
    # path('backend_bistro/<str:letter>/', views.menu_by_category),
    
]