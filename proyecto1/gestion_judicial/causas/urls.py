from django.urls import path
from . import views

app_name = 'causas'

urlpatterns = [
    path('', views.CausaListView.as_view(), name='lista'),
    path('<int:pk>/', views.CausaDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.CausaUpdateView.as_view(), name='editar'),
]
