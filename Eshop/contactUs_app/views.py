from django.shortcuts import render, redirect

from settings_app.models import SiteSettings
from contactUs_app.forms import ContactForm
from contactUs_app.models import Contact
from django.contrib import messages
from django.utils import html


# Create your views here.
def contact_us_view(request):
    setting = SiteSettings.objects.first()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        text = form.cleaned_data.get("text")

        new_contact = Contact.objects.create(name=name, email=email, subject=subject, text=text)
        if new_contact is not None:
            messages.success(request,
                             html.format_html("<p class='alert alert-success'>Your message has been sent</p>")
                             )
            return redirect("contact-us")
        else:
            form = ContactForm()
    context = {
        "setting": setting,
        "form": form,
    }
    return render(request, "contact_us/contact_us.html", context)
