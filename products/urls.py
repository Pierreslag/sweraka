from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),  # Added comma at the end
    path('<product_id>', views.product_detail, name='product_detail'),
]
