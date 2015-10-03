# -*- coding: utf-8 -*-
from django.shortcuts import render
 
def home(request):
    return render(request, "car_rental/index.html", {})