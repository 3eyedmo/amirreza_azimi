from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home/index.html')
    # return HttpResponse("سلام بچه ها")
