from django.urls import path


from .views import opinionview
urlpatterns=[
    path('opiniones/',opinionview.as_view(),name='opinio_list'),
    path('opiniones/<int:id>',opinionview.as_view(),name='opinion_list'),
    
]