from django.shortcuts import render, redirect
from .models import CounterModel


# Create your views here.


def helloworld(request):
    name = "surya"
    obj = CounterModel.objects.filter(id=1)[0]
    our_number = obj.number

    context = {'name': name, 'number': our_number}
    return render(request, "helloworld/helloworld.html", context)


def hellostudent(request):
    return render(request, "helloworld/hellostudent.html")


def increment(request):
    # Here we write code to increment a number
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) + 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])


def decrement(request):
    # here we will write code to decrement a number
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) - 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])


def reset(request):
    # Here we will write code to reset the number to 0
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

