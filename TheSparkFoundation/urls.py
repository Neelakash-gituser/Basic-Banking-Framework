from django.urls import path
from . import views

urlpatterns = [path('',views.home,name = 'home'),
    path('viewallcustomer',views.view,name = 'view'),
    path('viewallcustomer/<int:customer_id>/',views.customer_details,name='customer_details'),
    path('moneytransfer',views.transfer,name='transfer'),
]