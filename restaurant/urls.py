from django.urls import path

from . import views

urlpatterns = [

    path('',views.Deshboard.as_view(), name='Deshboard'),
    path('payment/', views.Order.as_view(), name='order'),
]