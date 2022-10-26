from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from itsdangerous import Serializer
from .models import Emp 
from demoapp.forms import EmpForm
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail

#task3
def email(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('empdata')
            except:
                pass
    else:
        form = EmpForm()
    return render(request, 'email.html', {"form": form})


def empdata(request):
    object = Emp.objects.all()
    return render(request, 'empdata.html', {'object': object})


def update_data(request, id):
    object = Emp.objects.get(id=id)
    if request.POST:
        if object:
            object.Empcode = request.POST['Empcode']
            object.Name =request.POST['Name']
            object.DOBirth =request.POST['DOBirth']
            object.DOJoining = request.POST['DOJoining']
            object.DOAnniversary = request.POST['DOAnniversary']
            object.Email = request.POST['Email']
            object.save()
        return redirect('empdata')
    return render(request, 'editdata.html', {'object': object})


def delete_data(request, id):
    object = Emp.objects.get(id=id)
    object.delete()
    return redirect('empdata')

def data(request):
    return redirect('edata')

def edata(request):
    today_date = datetime.today().date()
    birthdays = Emp.objects.filter(DOBirth__day=today_date.day,DOBirth__month=today_date.month)
    joining = Emp.objects.filter(DOJoining__day=today_date.day,DOJoining__month=today_date.month)
    annversary = Emp.objects.filter(DOAnniversary__day=today_date.day,DOAnniversary__month=today_date.month)
    return render(request, 'data.html',{'birthdays':birthdays, 'joining':joining, 'annversary':annversary})

def query(request):
    return redirect('mail')

def mail(request):
    return render(request,'message.html')



