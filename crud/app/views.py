from django.shortcuts import render,HttpResponse, redirect
from . models import crud
#from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse('Hello to Crud')
    courses = crud.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course/index.html', context)

def create(request):
    course = crud.objects.create(course_name=request.POST.get('course_name', False), description=request.POST.get('description', False))
    course.save()
    return redirect('/')

def remove(request, id):
    id= crud.objects.get(id=id)
    context ={
        'current_course':id
    }
    return render(request, 'course/remove.html', context)

def destroy(request, id):
    current_course = crud.objects.get(id=id)
    current_course.delete()
    return redirect('/')