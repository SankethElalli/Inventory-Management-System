from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/', views.list_products, name='list_products'),
    path('suppliers/add/', views.add_supplier, name='add_supplier'),
    path('suppliers/', views.list_suppliers, name='list_suppliers'),
    path('stock/add/', views.add_stock_movement, name='add_stock_movement'),
    path('sales/create/', views.create_sale_order, name='create_sale_order'),
    path('sales/cancel/<str:order_id>/', views.cancel_sale_order, name='cancel_sale_order'),
    path('sales/complete/<str:order_id>/', views.complete_sale_order, name='complete_sale_order'),
    path('sales/', views.list_sale_orders, name='list_sale_orders'),
    path('stock/check/', views.check_stock_levels, name='check_stock_levels'),
]

