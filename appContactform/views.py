from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        sender_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=sender_email, subject=subject, message=message)
        contact.save()
        
        html = render_to_string("email/contactform.html", {
                "name":name,
                "subject":subject,
                "sender_email":sender_email,
                "message":message,
            })
        
        send_mail(
            'İletişim Formu', 
            message, 
            settings.EMAIL_HOST_USER, 
            ['helloween_caner@hotmail.com'],
            fail_silently=False,
            html_message=html)

        

    context={}
    return render(request,'index.html',context)