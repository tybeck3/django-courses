from django.shortcuts import render, redirect
from . models import Course

def index(request):
    return render(request, 'index.html', {
        "all_courses": Course.objects.all()
    })

def add(request):
    Course.objects.create(
        title = request.POST['title'],
        description = request.POST['description']
    )
    return redirect('/')

def remove(request, id):
    return render(request, 'remove.html', {
        "course": Course.objects.get(id = id)
    })

def delete(request, id):
    to_delete = Course.objects.get(id = id)
    to_delete.delete()
    return redirect('/')