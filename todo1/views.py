from django.shortcuts import render, redirect

from .models import *
# Create your views here.

def home(request):
    if request.method == "POST":
        Reja.objects.create(
            vaqt = request.POST['v'],
            text = request.POST['text'],
            status = request.POST['h']
        )
        return redirect("/")
    content = {
        'todolar': Reja.objects.all()
    }
    return render(request, "todo_eski.html", content)

def reja_ochir(request, son):
    Reja.objects.get(id=son).delete()
    return redirect("/")