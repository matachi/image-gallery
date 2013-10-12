from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        sent_from = '{name} {email}'.format(name=name, email=email)
        subject = self.cleaned_data.get('subject')
        message = self.cleaned_data.get('message')
        recipient = get_user_model().objects.get(pk=1).email

        send_mail(subject, message, sent_from, [recipient])