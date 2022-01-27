from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from .models import Customer

class index(CreateView):
    model = Customer
    fields = '__all__'
    queryset = Customer.objects.all()
    template_name = "index.html"


def inv(request):
    names=Customer.objects.all()
    template = loader.get_template('index.html')
    context = {
        'queryset': names,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'index.html',context)