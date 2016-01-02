from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


from .mixins import BackgroundMixin
from .forms import ContactForm


class Index(BackgroundMixin, TemplateView):
    template_name = "index.html"
        

class About(BackgroundMixin, TemplateView):
    template_name = "about.html"


class Contact(BackgroundMixin, FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['sender']
        msg=form.cleaned_data['message']
        msg_plain = render_to_string('emails/contact_email.txt', {'name': name, 'email': email, 'msg': msg})
        send_mail('Pythad Blog letter', msg_plain,
                  settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        return super(Contact, self).form_valid(form)


class Resume(BackgroundMixin, TemplateView):
    template_name = "resume.html"
