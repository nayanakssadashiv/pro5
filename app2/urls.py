from django.urls import path
from app2 import views
app_name="app2"
urlpatterns = [
    path("index2/",views.index2,name="index2"),
    path("rend_app2/",views.rend_app2,name="rend_app2"),
]
