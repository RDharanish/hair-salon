from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment  


def appointment_view(request):
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
        return render(request,'success.html')

    
        messages.success(request, 'Your appointment has been successfully scheduled.')

        
       # return 'booked succesfully' 

    # If not a POST request, render the index.html
    return render(request, 'index.html')  
