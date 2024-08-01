from django.urls import path,include
from .views import *

urlpatterns=[
    path('show_attrition/', Attrition_rate_finder, name='attrition_show'),
]