from django.shortcuts import render
from .forms import LaptopModelForm,MobileModelForm,TVModelForm
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def Laptop(r):
    form = LaptopModelForm()
    if r.method =='POST':
        form = LaptopModelForm(r.POST)
        if form.is_valid():
            form.save()
    return render(r,'electronic/laptop.html',{'form':form})

def Mobile(r):
    form = MobileModelForm()
    if r.method =='POST':
        form = MobileModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index')
    return render(r,'electronic/mobile.html',{'form':form})

def TV(r):
    form = TVModelForm()
    if r.method =='POST':
        form = TVModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index')
    return render(r,'electronic/TV.html',{'form':form})

@login_required()
def laptopdetails(r):
    form = LaptopModel.objects.all()
    #form = LaptopModel.objects.filter(modelqnty__gt = 1)
    #form = LaptopModel.objects.filter(modelqnty__gte = 1)
    #form = LaptopModel.objects.filter(modelqnty__lt = 1)
    #form = LaptopModel.objects.filter(modelqnty__lte = 1)
    #form = LaptopModel.objects.filter(modelqnty__exact = 1)
    #form = LaptopModel.objects.filter(~Q(modelqnty__exact = 1))
    #form = LaptopModel.objects.filter(modelname__iexact='lenovo')
    #form = LaptopModel.objects.filter(modelname__icontains = 'l')
    #form = LaptopModel.objects.filter(modelname__icontains = 'no')
    #form = LaptopModel.objects.filter(modelname__contains = 'no') | LaptopModel.objects.filter(modelname__icontains = 'de')
    #form = LaptopModel.objects.filter(modelname__in = ['dell','HP'])
    #form = LaptopModel.objects.filter(modelname__istartswith = 'd') | LaptopModel.objects.filter(modelname__istartswith = 'l')
    #form = LaptopModel.objects.exclude(modelname__istartswith = 'd')
    #form = LaptopModel.objects.all().order_by('modelqnty')
    #form = LaptopModel.objects.all().order_by('-modelqnty')[2:3]
    return render(r, 'electronic/laptopdetail.html', {'laptop_list': form})

@login_required()
def lenovolaptopdetails(r):
    form = LaptopModel.objects.filter(modelname__iexact = 'lenovo')
    return render(r, 'electronic/laptopdetail.html', {'laptop_list': form})

def update(r,id):
    form = LaptopModel.objects.get(id=id)
    print(form)
    if r.method =='POST':
        form = LaptopModelForm(r.POST,instance=form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/electronic/laptopdetail/')
        return render(r, 'electronic/update.html', {'form': form})