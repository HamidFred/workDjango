from django.shortcuts import render, redirect, get_object_or_404
from .models import Table
from random import randint

def details(request,pk):
	obj = Table.objects.get(pk=pk)
	return render(request,'detailer.html',{'obj':obj})

def redi_by_name(request):
	pk = randint(0,49)
	return redirect('detail',pk)

def redi_by_url(request):
	pk = randint(49,49)
	return redirect('/'+str(pk)+'/')

def redi_by_obj(request):
	pk = randint(0,4)
	obj = Table.objects.get(pk=pk)
	return redirect(obj)

def redi_by_view(request,pk):
	return redirect(details,pk)

def rand(request):
	pk = randint(0,49)
	return redirect('detail',pk)