from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

class TovaryListView(ListView):
    model = Tovar
    template_name = 'tovary_list.html'
    context_object_name = 'tovars'

class TovaryCreateView(CreateView):
    model = Tovar
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('tovary')

class TovaryDeleteView(DeleteView):
    model = Tovar
    template_name = 'details.html'
    success_url = reverse_lazy('tovary')

class TovaryUpdateView(UpdateView):
    model = Tovar
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('tovary')

class TovaryDetailView(DetailView):
    model = Tovar
    template_name = 'details.html'
    context_object_name = 'tovars'








## Все товары, отдельная страница товара, Создание товара и его обновление, удаление товара