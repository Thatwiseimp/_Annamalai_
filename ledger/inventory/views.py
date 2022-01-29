from django.http import HttpResponse
from .models import Customer, MConfig,PType
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import add_customer_form


def index(request):
    inventory = Customer.objects.all()
    return HttpResponse(inventory.values())


class my_dictionary(dict):
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

def inv(request):
    store=[]

    cust_list = Customer.objects.all()
    for customer in cust_list:
        data = my_dictionary()
        data.add('name',customer.Customer_name)

        try:
            packet_list = MConfig.objects.filter(user__pk=customer.id)

            for i in packet_list:
                data.add(i.packet.label,i.quantity)
            store.append(data)



        except Exception as e:
            print(e)


        print(store)
    return render(request, 'index.html', {'store': store})


def profile(request,cust_id):
    return
    # try:
    #     packet_list = MConfig.objects.filter(user__pk=cust_id)
    #     total = 0
    #     for i in packet_list:
    #         total += i.packet.price * i.quantity
    #         print(total)
    # except Exception as e:
    #     print(e)


def add_customer(request):
    if request.method == 'POST':
        form = add_customer_form(request.POST)
        if form.is_valid():
            c = Customer(Customer_name=form.cleaned_data['name'], Phone_number=form.cleaned_data['number'])
            c.save()
            for label in PType.objects.all():
                id = MConfig.objects.all().count()+1
                mc = MConfig(user=c,packet=label)
                mc.save()
            return HttpResponseRedirect('thanks/')
    else:
        form = add_customer_form()
    return render(request, 'add_customer.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')