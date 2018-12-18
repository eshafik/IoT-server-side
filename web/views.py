import json, time

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.

alive = 0
data = {}

def home(request):
    return render(request,'index.html')

def keep_alive(request):
    print("Ok")
    post_id = request.POST.get('id')
    print(post_id)
    return JsonResponse({'status':'ok'})

#     if request.method == "POST":
#         print("Ok")
#         print(x)
#         global alive, data
#         alive += 1
#         keep_alive_count = str(alive)
#         data['keep_alive'] = keep_alive_count
#         parsed_json = json.dumps(data)
#         print(parsed_json)
#         # return str(parsed_json)
#         return HttpResponse("HI......")
def test(request,x):
    if request.method == "POST":
        print("OKPOST")
        print(x)