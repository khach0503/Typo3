from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets

from data.models import Customer


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html', context=None)

class Customers(TemplateView):
    def getCust(request):
        name='liran'
        return HttpResponse('{ "name":"' + name + '", "age":31, "city":"New York" }')


@api_view(["POST"])
def CalcTest(x1):
    try:
        x=json.loads(x1.body)
        y=str(x*200)
        return JsonResponse("Result:"+y,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def Stringret(strin):
    try:
        x=json.loads(strin.body.decode('utf-8'))
        y=str(x)
        xuly = StringIns(y)
        return JsonResponse(xuly,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
		
def StringIns(strin):
    leng = len(strin)-2
    if leng > 3:
        x = strin[0:leng]
    return x + "<<đã xóa đi 2 ký tự>>"

class CustSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'type')


class CustViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustSerializer