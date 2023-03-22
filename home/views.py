from django.shortcuts import render

def home(request):
    context={'titulo':'Inicio'}
    return render(request, 'home.html',context)