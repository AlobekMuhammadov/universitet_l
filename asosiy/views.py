from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def fan(request):
    if request.method == 'POST':
        Fan.objects.create(
            asosiy = request.POST.get('asosiy'),
            nom = request.POST.get('nom'),
            yonalish = Yonalish.objects.get(id=request.POST.get('y'))
        )
        return redirect('/fanlar/')


    soz = request.GET.get('search')
    if soz == '' or soz is None:
        content= {
            'fanlar':Fan.objects.all(),
            'yonalishlar': Yonalish.objects.all()
        }
    else:
        content = {
            'fanlar':Fan.objects.filter(nom__contains=soz),
            'yonalishlar':Yonalish.objects.all()
        }
    return render(request,'fan.html/', content)

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
        Yonalish.objects.create(
            aktiv = request.POST.get('aktiv'),
            nom = request.POST.get('nom')
        )
        return redirect('/yonalishlar/')


    soz = request.GET.get('search')
    if soz == '' or soz is None:
        content= {
            'yonalishlar': Yonalish.objects.all()
        }
    else:
        content = {
            'yonalishlar':Yonalish.objects.all()
        }
    return render(request,'yonalish.html/', content)



def yonalish_ochir(request,son):
    Yonalish.objects.filter(id=son).delete()
    return redirect('/yonalishlar/')



