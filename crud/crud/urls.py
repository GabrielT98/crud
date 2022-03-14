from crud import views
from django.urls import path

urlpatterns = [
    path('produto/',views.listar_produto),
    path('produto/<int:id>',views.ver_detalhes),
    path('adicionar/',views.adicionar_produto),
    path('delete/<int:id>',views.delete_produto)
]
