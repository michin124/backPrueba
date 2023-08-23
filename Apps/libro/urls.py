from django.urls import path


from .views import libroview
urlpatterns=[
    path('libro/',libroview.as_view(),name='libro_list'),
    path('libro/<int:id>',libroview.as_view(),name='libro_list'),
    path('libroCat/<int:categoria>',libroview.as_view(),name='libro_list'),
    path('libroU/<str:search>',libroview.as_view(),name='libro_list'),
]