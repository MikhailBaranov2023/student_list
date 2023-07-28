from django.views.generic import CreateView
from materials.models import Material
from django.urls import reverse_lazy


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
