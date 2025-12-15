from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='lista'),
    path('<int:pk>/', views.ClienteDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='editar'),
]
