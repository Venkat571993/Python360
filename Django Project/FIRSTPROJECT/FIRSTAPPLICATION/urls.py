from django.urls import path
from . import views


urlpatterns = [
    path('Homepage/',views.Homepage ),
    path('CustomerDetails/',views.All_customerDetails),
    path('Customer/<int:pk>/',views.single_customer),
]