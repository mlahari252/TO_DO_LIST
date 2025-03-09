from django.urls import path
from . import views
urlpatterns=[
    path('',views.To_do_list,name='list_name'),
    path('1/',views.home,name='home_name'),
    path('2/<int:pk>/',views.contact,name='contact_name'),
    path('3/<int:pk>/',views.edit,name='edit_name')
]