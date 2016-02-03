from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the poc index.")

def vinay(request):
	return HttpResponse("Ha Ha")