from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/tasks/',
        'Detail View': '/tasks/<int:id>/',
        'Create': '/tasks/',
        'Update': '/tasks/<int:id>/',
        'Delete': '/tasks/<int:id>/',
    }
    return Response(api_urls)