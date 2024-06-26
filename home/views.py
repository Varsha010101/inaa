from django.shortcuts import render, HttpResponse
from datetime import datetime
import subprocess
from django.utils import timezone
import os
from home.models import Contact
from django.contrib import messages

def index(request):
    return render (request,'index.html')
def contact(request):
    return render(request,"contact.html")
def main(request):
    return render(request,".main.py/")
def chat(request,community):
   return HttpResponse(community)
def execute_main(request):
    main_path = os.path.join(os.path.dirname(__file__), 'm123.py')
    subprocess.run(['python', main_path])
    return HttpResponse("executed")
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        date = timezone.now()
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            date=date
        )
        messages.success(request, "Profile details updated.")
    return render(request, 'contact.html')