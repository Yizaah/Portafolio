from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from django.db.models import Q
from movimientos.forms import MovimientoForm
from .forms import CausaForm
from .models import Causa, EstadoCausa
from django.urls import reverse_lazy

class CausaListView(ListView):
    model = Causa
    template_name = 'causas/causa_list.html'
    context_object_name = 'causas'
    paginate_by = 20

    def get_queryset(self):
        queryset = Causa.objects.select_related('cliente')

        # Mostrar solo causas activas por defecto
        estado = self.request.GET.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        else:
            queryset = queryset.filter(estado=EstadoCausa.ACTIVA)

        # Filtros 
        competencia = self.request.GET.get('competencia')
        if competencia:
            queryset = queryset.filter(competencia=competencia)

        tribunal = self.request.GET.get('tribunal')
        if tribunal:
            queryset = queryset.filter(tribunal__icontains=tribunal)

        tipo_causa = self.request.GET.get('tipo_causa')
        if tipo_causa:
            queryset = queryset.filter(tipo_causa__iexact=tipo_causa)

        rol = self.request.GET.get('rol')
        if rol:
            queryset = queryset.filter(rol=rol)

        anio = self.request.GET.get('anio')
        if anio:
            queryset = queryset.filter(anio=anio)

        # Búsqueda por cliente
        buscar_cliente = self.request.GET.get('cliente')
        if buscar_cliente:
            queryset = queryset.filter(
                Q(cliente__nombres__icontains=buscar_cliente) |
                Q(cliente__apellidos__icontains=buscar_cliente) |
                Q(cliente__rut__icontains=buscar_cliente)
            )

        return queryset

class CausaDetailView(DetailView):
    model = Causa
    template_name = 'causas/causa_detail.html'
    context_object_name = 'causa'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movimientos'] = self.object.movimientos.all()
        context['form'] = MovimientoForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = MovimientoForm(request.POST)

        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.causa = self.object
            movimiento.save()
            return redirect('causas:detalle', pk=self.object.pk)

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

class CausaUpdateView(UpdateView):
    model = Causa
    form_class = CausaForm
    template_name = 'causas/causa_form.html'

    def get_success_url(self):
        return reverse_lazy('causas:detalle', kwargs={'pk': self.object.pk})

