from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import CustomerDetail
from .serializers import CustomerDetails_Serializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def Homepage(request):
    return render(request,'FIRSTAPPLICATION/userinterface.html')


@csrf_exempt
def All_customerDetails(request):
    try:
        customers= CustomerDetail.objects.all()

    except:
        return HttpResponse("So Sorry!!! ,Not Found", status=404)
    
    if request.method == "GET":
        all_customers = CustomerDetails_Serializer(customers, many= True)
        return JsonResponse(all_customers.data,safe=False,status=200)
    
    elif request.method == "POST":
        input_data = JSONParser().parse(request)
        serializer = CustomerDetails_Serializer(data=input_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        else:
            return JsonResponse(serializer.errors,status=400)    


def single_customer(request, pk):
    try:
        customer= CustomerDetail.objects.get(pk=pk)
    except:
        return HttpResponse("So Sorry!!! ,Not Found", status=404)
    
    if request.method =="GET":
        single_customer = CustomerDetails_Serializer(customer)
        return JsonResponse(single_customer.data,status=200)
    



