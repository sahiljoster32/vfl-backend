from django.urls import path
from .views import VendorView, VendorCreateView

urlpatterns=[
    path('vendor/<int:pk>/', VendorView.as_view()),
    path('vendor/create/', VendorCreateView.as_view()),
]