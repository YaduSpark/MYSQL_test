from django.urls import path 

from mysql_app import views

urlpatterns = [
    path('product', views.ProductListView.as_view()),
    path('product/<int:pk>/', views.ProductDetailsView.as_view()),
    path('category', views.CategoryListView.as_view()),
    path('category/<int:pk>/', views.CategoryDetailsView.as_view()),
    path('manufacturer', views.ManufacturerListView.as_view()),
    path('manufacturer/<int:pk>/', views.ManufacturerDetailsView.as_view()),
]