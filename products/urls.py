from django.urls import path
from .views import ProductListCreateView, ProductDetailView


urlpatterns = [
    path("product/", ProductListCreateView.as_view(), name="product-list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product-detail")
]
