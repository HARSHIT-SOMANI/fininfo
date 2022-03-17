#usernme:dell pwd:1

from django.shortcuts import render
from .models import details

# Create your views here.
def home(request):
    return render(request,'index.html')

def showdb(request):
    if(request.method=='POST'):
        myuser=details.objects.create(name=request.POST['name'])
        myuser.dob=request.POST['dob']
        myuser.email=request.POST['email']
        myuser.street=request.POST['street']
        myuser.flat=request.POST['flat']
        myuser.country=request.POST['country']
        myuser.number=request.POST['number']
        myuser.gender=request.POST['gender']
        if len(request.FILES)!=0:
            myuser.image=request.FILES['image']
        myuser.save()
    last=details.objects.last()
    context={
        'name':last.name,
        'dob':last.dob,
        'email':last.email,
        'number':last.number,
        'gender':last.gender,
        'flat':last.flat,
        'street':last.street,
        'country':last.country,
        'image':last.image
    }
    return render(request,'db.html',context)