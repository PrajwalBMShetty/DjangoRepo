from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
   # return HttpResponse("Thsi  is my homepage(/)")
   context={'name':'Prajwal','course':'Python'}
   return render(request,'home.html',context)
def about(request):
   # return HttpResponse("Thsi  is my homepage(/)")
   return render(request,'about.html')
def projects(request):
   # return HttpResponse("Thsi  is my homepage(/)")
   return render(request,'projects.html')
def contact(request):
   if request.method=="POST":
     print("this is posts")
     name=request.POST['name']
     email=request.POST['email']
     phone=request.POST['phone']
     desc=request.POST['desc']
     print(name, email, phone, desc)
     ins=Contact(name=name, email=email, phone=phone, desc=desc)
     ins.save()
     print("data has written to db")
   # return HttpResponse("Thsi  is my homepage(/)")
   return render(request,'contact.html')





