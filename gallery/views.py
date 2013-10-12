# Create your views here.
from django.views.generic import ListView
from gallery.models import Image


class ImageList(ListView):
    model = Image
