import json, time

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum

from .models import Line, Production

# Create your views here.

alive = 0
data = {}

def home(request):
    return render(request,'index.html')

def keep_alive(request):
    if request.method == 'POST':
        print("Ok")
        data = request.POST.get('id')
        print(data)
        data = data.split(" ")
        line_value = int(data[0])
        production_value = int(data[1])
        if line_value in range(1,20):
            try:
                line = Line.objects.get(line_no=line_value)
            except:
                Line.objects.create(line_no=line_value)
                line = Line.objects.get(line_no=line_value)
                print("New line created")
            Production.objects.create(line=line,production_size=production_value)
            s = line.production.all()
            print(s)
        return JsonResponse({'status':'ok'})

def test(request):
    line = Line.objects.get(line_no=2)

    s = line.production.all().values('production_size')
    print(s)
    sum=0
    for i in s:
        print(type(i['production_size']))
        sum+= i['production_size']
    print(sum)
    return HttpResponse("HI")