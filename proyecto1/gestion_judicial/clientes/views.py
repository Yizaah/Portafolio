from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Cliente
from .forms import ClienteForm


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 20

    def get_queryset(self):
        queryset = Cliente.objects.all().order_by('apellidos', 'nombres')

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombres__icontains=query) |
                Q(apellidos__icontains=query) |
                Q(rut__icontains=query)
            )

        return queryset

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = 'cliente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['causas'] = self.object.causas.all().order_by('-anio')
        return context


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'

    def get_success_url(self):
        return reverse_lazy('clientes:detalle', kwargs={'pk': self.object.pk})