import json
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .serializers import *
from .forms import *

class APIProductCategoriesCreate(APIView):
	#permission_classes = (IsAuthenticated,)
	permission_classes = (AllowAny,)
	form_class = ProductCategoriesForm

	def get(self, request):
		return render(
            request,
            'ProductCategories.html',
            {
                'title':'Добавление категории товаров',
                'year':datetime.now().year,
				'form': self.form_class()
            },
        )

	def post(self, request, format=None):
		formdata = request.data.copy()
		prodcat = ProductCategories()
		prodcat.name = formdata['name']
		prodcat.save()
		
		#return Response(status=status.HTTP_201_CREATED)
		return HttpResponseRedirect('/productcategories/')

class APIProductCreate(APIView):
	#permission_classes = (IsAuthenticated,)
	permission_classes = (AllowAny,)
	form_class = ProductForm

	def get(self, request):
		return render(
            request,
            'Product.html',
            {
                'title':'Добавление нового товара',
                'year':datetime.now().year,
				'form': self.form_class()
            },
        )

	def post(self, request, format=None):
		formdata = request.data.copy()
		prodcat = Product()
		prodcat.name = formdata['name']
		prodcat.vendorcode = formdata['vendorcode']
		prodcat.description = formdata['description']
		prodcat.prodcat = formdata['prodcat']
		prodcat.save()
		
		#return Response(status=status.HTTP_201_CREATED)
		return HttpResponseRedirect('/product/')

class APIProductCategories(APIView):
	#permission_classes = (IsAuthenticated,)
	permission_classes = (AllowAny,)

	def get(self, request):
		try:
			prodcatid = request.GET['id']
		except:
			prodcatid = None

		if prodcatid:
			prodcat = get_object_or_404(ProductCategories, id=prodcatid)
		else:
			prodcat = ProductCategories.objects.all()

		if isinstance(prodcat, ProductCategories):
			prodcatdata = ProductCategoriesSerializer(prodcat).data
		else:
			prodcatdata = ProductCategoriesSerializer(prodcat, many = True).data

		return render(
            request,
            'ProductCategoriesList.html',
            {
                'title':'Категории товаров',
                'year':datetime.now().year,
                'prodcatdata': json.dumps(prodcatdata, ensure_ascii=False),
            },
        )
		#return Response(prodcatdata)
    
	def put(self, request, id, format=None):
		formdata = request.data.copy()
		#...
		return Response(status=status.HTTP_200_OK)

	def delete(self, request, id, format=None):
		try:
			prodcatobj = ProductCategories.objects.get(pk=id)
		except ProductCategories.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		prodcatobj.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class APIProduct(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		try:
			productid = request.GET['productid']
		except:
			productid = None

		if productid:
			product = get_object_or_404(Product, id=productid)
		else:
			product = Product.objects.all()

		if isinstance(product, Product):
			productdata = ProductSerializer(product).data
		else:
			productdata = ProductSerializer(product, many = True).data

		return render(
            request,
            'ProductList.html',
            {
                'title':'Товары',
                'year':datetime.now().year,
                'productdata': json.dumps(productdata, ensure_ascii=False),
            },
        )
		#return Response(status=status.HTTP_200_OK)

	def post(self, request, format=None):
		formdata = request.data.copy()
		#...
		return Response(status=status.HTTP_201_CREATED)
    
	def put(self, request, id, format=None):
		formdata = request.data.copy()
		#...
		return Response(status=status.HTTP_200_OK)

	def delete(self, request, id, format=None):
		try:
			productobj = Product.objects.get(pk=id)
		except Product.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		productobj.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)