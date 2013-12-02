from models import Production, Elementary, Category, New
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list(request):
	"""
	"""
	data 		= serializers.serialize("python", Category.objects.all())
	page 		= request.GET.get("page")
	topic 		= request.GET.get("topic")
	if page == None: page = 1
	if topic == None: topic = "None"
	product_list = serializers.serialize("python", Production.objects.filter(product_category_en = Category.objects.filter(name_en = topic)))
	if len(product_list) == 0:	contacts = None
	else:	
		paginator = Paginator(product_list, 10)
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
			contacts = paginator.page(paginator.num_pages)
	return render_to_response('home/product_list.html', context_instance = RequestContext(request, {
			'objects': data,
			'items_list': contacts,
		}))

def home_page(request):
	"""
	"""
	new_list = New.objects.all()
	return render_to_response('home/home_page.html', context_instance = RequestContext(request,{
		"new_list": new_list,
		}))

def perspective(request):
	"""
	"""
	return render_to_response('home/home_perspective.html', context_instance = RequestContext(request))
