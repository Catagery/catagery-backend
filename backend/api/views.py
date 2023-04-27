from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import random
import datetime
import json
# Create your views here.


@api_view(['GET'])
def main_page(request):
    customer = User.objects.get(id=1).customer
    customer_serializer = CustomerSerializer(customer, many=False)
    
    purchases = Purchase.get_categoried_purchases('Games', customer)
    purchases_serializer = PurchaseSerializer(purchases, many=True)
    
    response = {
                'customer':customer_serializer.data, 
                'purchases':purchases_serializer.data
                }
    
    return Response(response, status=200)


@api_view(['GET'])
def get_rangom_grafic_info(request):
    categories = Category.objects.all().order_by('-title')
    categories_serializer = CategorySerializer(categories, many=True)
    
    customer = User.objects.get(id=1).customer
    customer_serializer = CustomerSerializer(customer, many=False)
    
    categ = categories[random.randint(0, categories.count()-1)]
    categ_serializer = CategorySerializer(categ)
    
    purchase = Purchase.get_categoried_purchases(categ, customer)
    purchaseserializer = PurchaseSerializer(purchase, many=True)
    if len(purchase) != 0:
        response = {
            'CategoryGrafic':purchaseserializer.data,
            'Categories':categories_serializer.data,
            'Category':categ_serializer.data,
            'found': True
        }
    else:
        response = {
            'Categories':categories_serializer.data,
            'Category':categ_serializer.data,
            'found': False
        }
    return Response(response)


@api_view(['GET'])
def get_grafic_info(request, category: str):
    categories = Category.objects.all()
    categories_serializer = CategorySerializer(categories, many=True)
    selected_category = Category.objects.get(title=category)
    print(selected_category)
    selected_category_serializer = CategorySerializer(selected_category, many=False)
    
    customer = User.objects.get(id=1).customer
    customer_serializer = CustomerSerializer(customer, many=False)
    
    purchase = Purchase.get_categoried_purchases(selected_category, customer)
    purchaseserializer = PurchaseSerializer(purchase, many=True)

    if len(purchase) != 0:
       response = {
           'CategoryGrafic':purchaseserializer.data,
           'Categories':categories_serializer.data,
           'Category':selected_category_serializer.data,
           'found': True
       }
    else:
       response = {
           'Categories':categories_serializer.data,
           'Category':selected_category_serializer.data,
           'found': False
       }
    return Response(response)


@api_view(['GET'])
def get_grafic_info_by_date(request, category: str, start_date: str, end_date: str):
    Start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    End_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    
    categories = Category.objects.all()
    categories_serializer = CategorySerializer(categories, many=True)
    selected_category = Category.objects.get(title=category)
    # selected_category_serializer = CategorySerializer(selected_category, many=False)
    
    customer = User.objects.get(id=1).customer
    customer_serializer = CustomerSerializer(customer, many=False)
    
    purchase = Purchase.objects.filter(category=selected_category, customer=customer, date__range=[Start_date, End_date])
    purchaseserializer = PurchaseSerializer(purchase, many=True)

    response = {
        'CategoryGrafic':purchaseserializer.data,
        'Categories':categories_serializer.data
    }
    return Response(response)



@api_view(['GET'])
def get_top_categories(request):
    categories = Category.objects.all().order_by('-total_spend')
    categories_serializer = CategorySerializer(categories, many=True)
    top_categories_serializer = CategorySerializer(categories[:3], many=True)
    
    return Response({
        'top_categories':top_categories_serializer.data,
        'all_categories':categories_serializer.data
        })
    
    
@api_view(["GET"])
def get_recent_purchases(request):
    customer = User.objects.get(id=1).customer
    customer_serializer = CustomerSerializer(customer, many=False)
    
    purchases = Purchase.objects.filter(customer=customer).order_by("-date")[:4]
    purchases_serializer = PurchaseSerializer(purchases, many=True)
    
    return Response({
        'recentPurchases':purchases_serializer.data,
        })
    
    
@api_view(["POST"])
def purchases(request):
    data = json.loads(request.body)
    spended_sum = data['sum']
    if spended_sum > 0:
        category: Category = Category.objects.get(title=data['category'])
        Purchase.objects.create(category=category, price=spended_sum, customer=User.objects.get(id=1).customer)
        category.total_spend += spended_sum
        category.save()
        return Response({'status': 200})
    else:
        return Response({"status":404})

    
@api_view(["POST", "GET"])
def categories(request):
    if request.method == "POST":
        data = json.loads(request.body)
        category = data["category"]
        if Category.objects.filter(title=category, customer=User.objects.get(id=1).customer).exists() or category == "":
            return Response({'created': False})
        else:
            Category.objects.create(title=category, customer=User.objects.get(id=1).customer, color=data["color"])
            return Response({'created': True})
    else:
        customer = User.objects.get(id=1).customer
    
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        
        return Response({
            'categories':categories_serializer.data
        })