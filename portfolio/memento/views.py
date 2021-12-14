from django.contrib import messages
from django.shortcuts import render
from .models import Project, Resume
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

from decouple import config


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")

            context = {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message,
                "resume": Resume.objects.all(),
            }

            try:
                msg_plain = render_to_string("mail/contact.txt", context)

                send_mail(
                    "PORTFOLIO MESSAGE",
                    msg_plain,
                    config(EMAIL_USER),
                    [
                        config(MY_EMAIL),
                    ],
                )
            except:
                pass

            messages.info(request, "Your message has been sent successfully")
    else:
        form = ContactForm()

    context = {
        "projects": Project.objects.all(),
        "form": form,
    }
    return render(request, "index.html", context)
