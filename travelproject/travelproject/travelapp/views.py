from django.shortcuts import render
from .models import Place,Team
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')
def index(request):
    obj=Place.objects.all()
    team=Team.objects.all()
    return render(request,'index.html',{'result':obj,'t':team})
def about(request):
    return HttpResponse("ABOUT PAGE")
def contact(request):
    return render(request, 'contact.html')
def detail(request):
    return render(request,'detail.html')
def thanks(request):
    return HttpResponse("THANK YOU!!!!")

