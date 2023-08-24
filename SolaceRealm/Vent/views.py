from django.shortcuts import render
from django.http import HttpResponse
import datetime
from Vent import models

def index(request):
    return HttpResponse("Hello, Faj. You're at the HomePage.")

def diary(request):
    if request.method == "POST":
        print("poooooost!")
        title = request.POST['title']
        entry = request.POST['entry']
        ins = models.venttable(title=title,content=entry)
        ins.save()
        print(title,entry)
        return index(request)
    else:
        datetime1 = datetime.datetime.now()
        context = {'datetime':datetime1,'day': datetime1.strftime("%A")}
        print(context)
        return render(request,"base.html",context)

