from django.urls import path


from .views import userview
urlpatterns=[
    path('user/',userview.as_view(),name='user_list'),
    path('user/<int:id>/',userview.as_view(),name='user_list'),
    path('user/',userview.as_view(),name='user_list'),
    path('ini/<str:correo>/<str:password>',userview.as_view(),name='user_list'),
    path('users/<str:email>',userview.as_view(),name='user_list'),
    path('pregunta/<int:idP>',userview.as_view(),name='user_list'),
    path('confirm/<int:id>/',userview.as_view(),name='user_list'),
    path('login/<str:valid>/',userview.as_view(),name='user_list'),
]