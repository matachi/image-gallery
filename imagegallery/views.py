from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from imagegallery.forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'The email was successfully sent.')
        return super(ContactView, self).form_valid(form)

    @staticmethod
    def get_success_url():
        return reverse('contact')