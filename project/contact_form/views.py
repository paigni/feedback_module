from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def contactform(request):
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['name']
            phone = form1.cleaned_data['phone']
            message = form1.cleaned_data['message']
            try:
                send_mail(name, phone, message, ['info@domain.ru'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        form1 = ContactForm()
    return render(request, 'contact_form.html', {'form1': form1})