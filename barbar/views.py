from django.shortcuts import render, redirect
from django.contrib import messages
from barber.models import Appointment  

def homePage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_address = request.POST.get('email_address')
        phone = request.POST.get('phone')
        category = request.POST.get('category')
        date = request.POST.get('date')
        message = request.POST.get('message')

        appointment = Appointment(
            name=name,
            email_address=email_address,
            phone=phone,
            category=category,
            date=date,
            message=message
        )
        appointment.save()

        
        messages.success(request, 'Your appointment has been successfully scheduled.')

        return render('booked successfully')

    return render(request, "index.html")  