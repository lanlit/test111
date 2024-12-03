from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.

def course_list(request):
    courses = course.objects.all()
    return render(request,"list.html",{"ff":courses})

def A (request):
    id = request.GET.get("id", "")
    courses = course.objects.filter(id=id)
    return render(request,"A.html",{"ff":courses})

def B (request):
    name = request.GET.get("name", "")
    B = course.objects.filter(name=name)
    return render(request,"B.html",{"a":B})
    
class C(UpdateView):
    model = course
    fields = ["name","teacter"]
    template_name = "C.html"
    success_url = reverse_lazy("course_list")

class D(DeleteView):
    model = course
    template_name = "D.html"
    success_url = reverse_lazy("course_list")
