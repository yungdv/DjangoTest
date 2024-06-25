from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def groups(request):
    return render(request, 'main/groups.html')

def files(request):
    return render(request, 'main/files.html')
