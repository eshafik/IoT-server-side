import json, time

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum
from django.utils import timezone

from .models import Line, Production
from .forms import DateForm

# Create your views here.


# Query by date function
def query_data(start,end):
    prodcutions=0
    line_data =[]
    if start== end:
        date = start
        print(date)
        #for the query date, query all production for all line 
        productions = Production.objects.filter(production_date__date=date).order_by('-production_date')
        line_data = []
        #total line query
        total_line = Line.objects.all().values('line_no').order_by('line_no')
        
        #for every line, query the production and append the query result to the list
        for line in total_line:
            #first query the specific line object, then by related name find production
            temp = Line.objects.get(line_no=line['line_no']).production.filter(production_date__date=date).order_by('-production_date').values('production_size')
            sum = 0
            # sum all the production of the specific single line
            for i in temp:
                sum+= i['production_size']
            #append data to the list
            line_data.append(sum)
    else:   
        #for the query date, query all production for all line 
        productions = Production.objects.filter(production_date__date__range=[start, end]).order_by('-production_date')
        line_data = []
        #total line query
        total_line = Line.objects.all().values('line_no').order_by('line_no')
        
        #for every line, query the production and append the query result to the list
        for line in total_line:
            #first query the specific line object, then by related name find production
            temp = Line.objects.get(line_no=line['line_no']).production.filter(production_date__date__range=[start, end]).order_by('-production_date').values('production_size')
            sum = 0
            # sum all the production of the specific single line
            for i in temp:
                sum+= i['production_size']
            #append data to the list
            line_data.append(sum)
    return productions, line_data
            

def home(request):
    return render(request,'web/index.html')

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
    return render(request,'web/index.html')

def get_data(request):
    if request.method == "POST":
        dateForm = DateForm(request.POST)
        if dateForm.is_valid():
            #clean date range from the form
            start = dateForm.cleaned_data['start']
            end = dateForm.cleaned_data['end']
            productions, line_data = query_data(start,end)

            return render(request,'web/production_data.html',{'productions':productions,'line_data':line_data})
    else:
        dateForm = DateForm()
    return render(request,'web/date.html',{'form':dateForm})

def today_data(request):
    date = timezone.now().date()
    print(date)
    productions, line_data = query_data(date,date)

    return render(request,'web/production_data.html',{'productions':productions,'line_data':line_data})

def prodcution_data(request):
    return render(request,'web/production_data.html')