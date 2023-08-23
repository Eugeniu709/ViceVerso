from django.http import HttpResponse
from django.shortcuts import render


def viceverso (request):
	return render(request, 'viceverso.html')