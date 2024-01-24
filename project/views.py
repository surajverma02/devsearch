from django.shortcuts import render, redirect
from project.models import Project
from project.forms import ProjectForm

# Create your views here.

def get_projects(request):
    projects = Project.objects.all()
    return render(request, 'project/project.html' , {'projects':projects})

def get_projectsDetail(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'project/single-project.html' , {'project':projectObj,})

def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('get_projects')
        
    return render(request, 'project/project-form.html' , {'form':form})

def update_project(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('get_projects')
    return render(request, 'project/project-form.html' , {'form':form})

def delete_project(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('get_projects')
    
    return render(request, 'project/delete-confirm.html' , {'object':project})