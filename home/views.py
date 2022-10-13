from django.shortcuts import render
from django.core.mail import EmailMessage


def index(request):
    if request.method =="POST":
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        code = request.POST.get("codearea")
        file = request.FILES.getlist("codefile")
        emailmsg=EmailMessage(subject,code,'email or name',[email],)
        for f in file:
            emailmsg.attach(f.name, f.read(), f.content_type)
        emailmsg.send()
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')




