from django.shortcuts import render,redirect
from hospitalapp.models import Appointment, Patient
from hospitalapp.forms import AppointmentForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def inner(request):
    return render(request,'inner-page.html')
def about(request):
    return render(request,'about.html')

def doctor(request):
    return render(request ,'doctors.html')

def appointment(request):
    if request.method == 'POST':
        appointments = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message']


        )
        appointments.save()
        return redirect("/appointments")
    else :
        return render(request,'appointment.html')

def show(request):
    myappointments = Appointment.objects.all()
    return render(request, 'show.html', {'appointment':myappointments} )

def delete(request,id):
    appointment1 = Appointment.objects.get(id=id)
    appointment1.delete()
    return redirect("/show")



def edit(request,id):
   editappointment=Appointment.objects.get(id=id)
   return render(request,'edit.html',{'appointment':editappointment})

def update(request , id):
    updateinfo=Appointment.objects.get(id=id)
    form =AppointmentForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'appointment.html')