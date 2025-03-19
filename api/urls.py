from django.urls import path
from .views import ClienteList, GastoConductorList, gastoConductorListReload

urlpatterns = [
    path('v1/clientes',ClienteList.as_view(),name='cliente_list'),
    path('v1/gastos',GastoConductorList.as_view(),name='gastos_list'),
    path('v1/gastos/reload/',gastoConductorListReload,name='gastos_list_reload'),
    # path('v1/gastos/reload/(?:page-(?P<page_number>[0-9]+)/)?$',gastoConductorListReload,name='gastos_list_reload'),
]