from itertools import product
from django.shortcuts import render, redirect
from .forms import SubForm, EmailForm
from .models import EmailSub
from functions.auto_mail import auto_mail

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        else:
            return render(request, 'newsletter/register.html', {"form": form, "mail": "false"})
        return render(request, 'newsletter/thanks.html', {"form": form})
            #return redirect('/')
    else:
        form = SubForm()
    print(request.POST)
    return render(request, 'newsletter/register.html', {"form": form})


def test(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # print(request.POST)
            users = EmailSub.objects.all()
            c = 0
            for user in users:
                print(user.em_address, request.POST['content'], request.POST['subject'])
                auto_mail(user.em_address, request.POST['content'], request.POST['subject'])

            email = form.save(commit=False)
            email.save()
            return render(request, 'newsletter/sent.html', {"form": form})

    else:
        form = EmailForm()
    return render(request, 'newsletter/test.html', {"form": form})