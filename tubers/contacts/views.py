from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.


def contactTeam(request):

    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']
        tuber_id = request.POST['tuber_id']
        user_id = request.POST['user_id']

    # Todo for validating each variable
    contact = Contact(full_name=full_name, phone=phone, email=email, company_name=company_name, subject=subject,
                      message=message, tuber_id=tuber_id, user_id=user_id)
    contact.save()
    messages.success(request, 'Thanks for reaching out!')
    return redirect('webpages')
