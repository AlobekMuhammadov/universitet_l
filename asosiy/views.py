from django.shortcuts import render, redirect

from .forms import FanForm
from .models import *
from django.http import HttpResponse

def fanlar(request):
    if request.method == 'POST':
        forma = FanForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/asosiy/')
    fan = request.GET.get('qidiruv')
    if fan == "" or fan is None:
        content = {
            "fanlar": Fan.objects.all(),
            "yonalishlar" : Yonalish.objects.all(),
            "forma": FanForm()
        }
    else:
        content = {
            "fanlar": Fan.objects.filter(nom__icontains=fan),
            "yonalishlar": Yonalish.objects.all(),
            "forma": FanForm()
        }

    return render(request,'fan.html',content)

def fan_ochir(request, son):
    Fan.objects.filter(id=son).delete()
    return redirect('/fanlar/')



def ustoz(request):
    if request.method == 'POST':
        Ustoz.objects.create(
            ism = request.POST.get('ism'),
            daraja = request.POST.get('daraja'),
            yosh = request.POST.get('yosh'),
            jins = request.POST.get('jins'),
            fan = Fan.objects.get(id=request.POST.get('f'))
        )
        return redirect('/ustozlar/')



    soz = request.GET.get('search')
    if soz == '' or soz is None:
        content= {
            'ustozlar':Ustoz.objects.all(),
            'fanlar':Fan.objects.all()
        }
    else:
        content = {
            'ustozlar':Ustoz.objects.filter(ism__contains=soz),
            'fanlar': Fan.objects.all()
        }
    return render(request,'ustoz.html/', content)

def ustoz_ochir(request, son):
    Ustoz.objects.filter(id=son).delete()
    return redirect('/ustozlar/')



def yonalish(request):
    if request.method == 'POST':
        f =YonalishForm(request.POST)
        if f.is_valid():
            Yonalish.objects.create(
                nom=f.cleaned_data['nom'],
                aktiv=f.cleaned_data['aktiv']

        )
        return redirect('/yonalishlar/')
    content = {
        "yonalishlar" : Yonalish.objects.all(),
        "forma": YonalishForm
    }
    return render(request,'yonalish.html',content)



def yonalish_ochir(request,son):
    Yonalish.objects.filter(id=son).delete()
    return redirect('/yonalishlar/')



