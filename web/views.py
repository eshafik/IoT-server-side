import json, time

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.writer.excel import save_virtual_workbook


from .models import Line, Production
from .forms import DateForm

# Create your views here.


# Query by date function

def query_data(start,end):
    prodcutions=0
    line_data =[]
    line_column = []
    if start== end:
        date = start
        # print(date)
        #for the query date, query all production for all line 
        productions = Production.objects.filter(production_date__date=date).order_by('-production_date')
        #total line query
        total_line = Line.objects.all().values('line_no').order_by('line_no')
        
        s=0
        #for every line, query the production and append the query result to the list
        for line in total_line:
            s = s+1
            line_column.append("Line No: {}".format(s))
            #first query the specific line object, then by related name find production
            temp = Line.objects.get(line_no=line['line_no']).production.filter(production_date__date=date).order_by('-production_date').values('production_size')
            sum = 0
            # sum all the production of the specific single line
            for i in temp:
                sum+= i['production_size']
            #append data to the list
            line_data.append(sum)
        # print(line_column)
    else:   
        #for the query date, query all production for all line 
        productions = Production.objects.filter(production_date__date__range=[start, end]).order_by('-production_date')

        #total line query
        total_line = Line.objects.all().values('line_no').order_by('line_no')
        
        s=0
        #for every line, query the production and append the query result to the list
        for line in total_line:
            s = s+1
            line_column.append("Line No: {}".format(s))
            #first query the specific line object, then by related name find production
            temp = Line.objects.get(line_no=line['line_no']).production.filter(production_date__date__range=[start, end]).order_by('-production_date').values('production_size')
            sum = 0
            # sum all the production of the specific single line
            for i in temp:
                sum+= i['production_size']
            #append data to the list
            line_data.append(sum)
    return productions, line_data,line_column
            

def home(request):
    return render(request,'web/index.html')
@csrf_exempt
def keep_alive(request):
    if request.method == 'POST':
        print("Ok")
        data = request.POST.get('id')
        print(data)
        date = timezone.localtime(timezone.now())
        #print(date)
        date = date.strftime('%d/%m/%Y  %I:%M:%S %p')
        print(date)
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
            # s = line.production.all()
            # print(s)
        return JsonResponse({'status':'ok','date':date})

def test(request):
    line = Line.objects.get(line_no=2)

    s = line.production.all().values('production_size')
    # print(s)
    sum=0
    for i in s:
        # print(type(i['production_size']))
        sum+= i['production_size']
    # print(sum)
    return render(request,'web/index.html')

def get_data(request):
    if request.method == "POST":
        dateForm = DateForm(request.POST)
        if dateForm.is_valid():
            #clean date range from the form
            start = dateForm.cleaned_data['start']
            end = dateForm.cleaned_data['end']
            productions, line_data,line_column = query_data(start,end)

            return render(request,'web/production_data.html',{'productions':productions,'line_data':line_data})
    else:
        dateForm = DateForm()
    return render(request,'web/get_data.html',{'form':dateForm})

def today_data(request):
    date = timezone.now().date()
    # print(date)
    productions, line_data,line_column = query_data(date,date)
    
    return render(request,'web/production_data.html',{'productions':productions,'line_data':line_data})

def prodcution_data(request):
    return render(request,'web/production_data.html')

def export_to_excel(request):
    if request.method == "POST":
        dateForm = DateForm(request.POST)
        if dateForm.is_valid():
            #clean date range from the form
            start = dateForm.cleaned_data['start']
            end = dateForm.cleaned_data['end']
            productions, line_data,line_column = query_data(start,end)
            

            wb = Workbook(write_only=True)
            ws = wb.create_sheet('test')
            ws.append(line_column)
            ws.append(line_data)
            
            ws.append(["Line","Production Size", "Production Date", "Production Time"])
            for p in productions:
                ws.append([p.line.line_no,p.production_size,p.production_date.date(),p.production_date.time()])

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=mydata.xlsx'
            wb.save(response)
            return response
    else:
        dateForm = DateForm()
    return render(request,'web/get_excel.html',{'form':dateForm})

def monitr(request):
    return render(request,'web/monitor.html')