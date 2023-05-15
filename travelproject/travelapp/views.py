from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team
# Create your views here.
def demo(request):
    obj= place.objects.all()
    obj= team.objects.all()

    return render(request,"index.html",{'outcome':obj})
#def addition(request):
   # x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
    #sum=int(x+y)
   # return render(request, "result.html", {'result': sum})

#def subtraction(request):
    #a=int(request.GET['num3'])
    #b=int(request.GET['num4'])
    #c=int(a-b)

   # return render(request, "result.html", {'answer':c})

#def multiplication(request):
   # l=int(request.GET['num5'])
    #m=int(request.GET['num6'])
    ##n=int(l*m)
   # return render(request,"result.html",{'product':n})
#def division(request):
    #p=int(request.GET['num7'])
    #q=int(request.GET['num8'])
    #r=int(p/q)
    #return render(request,"result.html",{'quotient':r})
