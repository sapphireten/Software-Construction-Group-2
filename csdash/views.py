from django.shortcuts import render
from csdash.models import facultyModel

def showfac(request):
    showall = facultyModel.objects.all()
    return render(request,'index.html',{"data":showall})
    