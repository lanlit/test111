from .views import *
from django.urls import path,include 


urlpatterns = [
    path('',course_list, name="course_list"),
    path('A/', A,name="A"),
    path('B/', B,name="B"),
    path("C/<str:pk>/", C.as_view(),name="C"),
    path("D/<str:pk>/", D.as_view(),name="D"),


]
