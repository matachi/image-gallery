from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView
from gallery.models import Image


class ImageList(ListView):
    model = Image


class ImageCreate(CreateView):
    model = Image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = reverse('gallery:upload')
        return context

    def form_valid(self, form):
        messages.success(self.request, 'The image was successfully uploaded.')
        return super().form_valid(form)

    @staticmethod
    def get_success_url():
        return reverse('gallery:upload')
