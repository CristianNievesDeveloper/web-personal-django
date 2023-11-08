# enviaemail/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.template.loader import render_to_string

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'message': message
            })
            
            send_mail('subject', 'message', 'diegonieves1012@gmail.com', ['cristiannievesdeveloper@gmail.com'], html_message=html)
            return redirect('contact')
    else:
        form = ContactForm()
     
    return render(request, 'contact/contact.html',{
        "form": form
    })
