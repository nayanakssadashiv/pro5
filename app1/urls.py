from django.urls import path
from app1 import views
app_name="app1"
urlpatterns = [
    path("index1/",views.index1,name="index1"),
    path("rend_app1/",views.rend_app1,name="rend_app1"),
    path("<data>/",views.ulr_data,name="data"),
    path("fact/<num>/",views.fact_num,name="factorial"),
    path("add/<num1>/<num2>/",views.add,name="addition"),
]
