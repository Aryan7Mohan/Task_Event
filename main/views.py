from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events
from django.contrib import messages
from django.urls import reverse_lazy, reverse
# Create your views here.





def Like(response):
    if response.method=="POST":
        
        data=Events.objects.all()
        var=response.POST.get("like")
        arr={'key':'3','name':'random'}
        var2=Events.objects.filter(event_name=response.POST.get("like"))
        var3=Events.objects.filter(event_name=response.POST.get("like")).values("is_liked")
        if var3[0].get('is_liked')==True:
            Events.objects.filter(event_name=response.POST.get("like")).update(is_liked=False)
            arr={'key':'1','name':response.POST.get("like")}
        elif var3[0].get('is_liked')==False:
            Events.objects.filter(event_name=response.POST.get("like")).update(is_liked=True)
            arr={'key':'0','name':response.POST.get("like")}


        return render(response, 'main/events.html', {'data':data,'arr':arr})


def index(response):


    data=Events.objects.all()
    print("\n\n\nwhy:\n",data)
    if response.method=="POST":
        if response.POST.get("event_name") and response.POST.get("data") and response.POST.get("time"):
            saverecord = Events()
            saverecord.event_name = response.POST.get("event_name")
            saverecord.data = response.POST.get("data")
            saverecord.time = response.POST.get("time")
            saverecord.location = response.POST.get("location")
            saverecord.image= response.FILES['image']
            saverecord.save()
            messages.success(response, "Record saved successfully!!")
            return render(response, 'main/events.html', {'data':data})
    else:
        return render(response, 'main/events.html', {'data':data})


    

def form(response):


    return render(response, "main/form.html", {})


