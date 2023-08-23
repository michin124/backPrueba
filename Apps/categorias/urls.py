from django.urls import path


from .views import categoriaview
urlpatterns=[
    path('categoria/',categoriaview.as_view(),name='categoria_list'),
    path('categoria/<int:id>',categoriaview.as_view(),name='categoria_list'),
    
]