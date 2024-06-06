from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from shoppinghyx import settings
from django.contrib import messages
import random

# Create your views here.

def data(request):
    appointments = apoiment.objects.all()
    return render(request, 'data.html', {'appointments': appointments})


from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import Apoimentf
from .models import apoiment

def index(request):
    if request.method == 'POST':
        form = Apoimentf(request.POST)
        coname = request.POST.get('name')
        comail = request.POST.get('mail')
        cotime = request.POST.get('time')
        copho = request.POST.get('pho')
        comsg = request.POST.get('msg')

        if apoiment.objects.filter(mail=comail).exists():
            print("Email already exists")
            # Optionally, you can display a message to the user or redirect to another page
        else:
            if form.is_valid():
                try:
                    form.save()
                    print("Form data saved successfully")
                except Exception as e:
                    print(f"Error saving form data: {e}")
                
                sender_name = coname
                sender_mail = comail
                sender_msg = comsg
                sender_time = cotime
                sender_pho = copho
                sub = "New appointment"
                msg = f"NAME: {sender_name}\nMAIL: {sender_mail}\nPHONE: {sender_pho}\nTIME: {sender_time}\nMESSAGE: {sender_msg}"
                from_mail = settings.EMAIL_HOST_USER
                to_gmail = ["maulikmendpara2242@gmail.com"]
                try:
                    send_mail(subject=sub, message=msg, from_email=from_mail, recipient_list=to_gmail)
                    print("Email sent successfully")
                except Exception as e:
                    print(f"Error sending email: {e}")

                return redirect('index')
            else:
                print("Form is not valid")
                print(form.errors)

    else:
        form = Apoimentf()

    return render(request, 'index.html', {'form': form})

def book_appointment(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        try:
            appointment = apoiment.objects.get(id=appointment_id)
            sub = "Appointment Confirmation"
            msg = f"Dear {appointment.name},\n\nYour appointment has been booked successfully.\n\nDetails:\nDate: {appointment.time}\nMessage: {appointment.msg}\n\nThank you."
            from_mail = settings.EMAIL_HOST_USER
            to_mail = [appointment.mail]
            send_mail(subject=sub, message=msg, from_email=from_mail, recipient_list=to_mail)
            print("Email sent successfully")
        except apoiment.DoesNotExist:
            print(f"Appointment with ID {appointment_id} does not exist")
        except Exception as e:
            print(f"Error sending email: {e}")

        return redirect('data')

def update_appointment_time(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        new_time = request.POST.get('new_time')
        try:
            appointment = apoiment.objects.get(id=appointment_id)
            appointment.time = new_time
            appointment.save()
            print(f"Appointment with ID {appointment_id} updated successfully")
        except apoiment.DoesNotExist:
            print(f"Appointment with ID {appointment_id} does not exist")
        except Exception as e:
            print(f"Error updating appointment: {e}")

        return redirect('data')


def contact(request):
    # user=request.session.get('user')
    # final = usersignup.objects.get(gmail=user)
    # if request.method =='POST':
    #     coname = request.POST['firstname']
    #     comail = request.POST['gmail']
    #     comsg = request.POST['messege']

    #     sender_name = coname
    #     sender_mail = comail
    #     sender_msg  = comsg
    #     sub="New requast"
    #     msg = f"NAME: {sender_name}\n MAIL:{sender_mail}.\n{sender_msg}"
    #     from_mail = settings.EMAIL_HOST_USER
    #     to_gmail = ["maulikmendpara2242@gmail.com"]
    #     send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_gmail), {'user':user,'final':final}


    return render(request, 'contact.html')


def userlogout(request): 
    logout(request)
    return redirect('/')