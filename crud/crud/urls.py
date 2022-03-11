from crud import views
from django.urls import path

urlpatterns = [
    path('produto/',views.listar_produto),
    path('produto/<int:id>',views.ver_detalhes)
]
