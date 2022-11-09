from django.urls import path

from . import views

urlpatterns = [
    path('backend_bistro/', views.get_menu),
]