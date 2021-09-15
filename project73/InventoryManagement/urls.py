from django.urls import path
from . import views

urlpatterns =[
    path('create/',views.createorderview,name='addorder'),
    path('retrieve/',views.showorderview,name='showorder'),
    path('del/<int:id_form>',views.deleteorderview,name='delete'),
    path('upda/<int:id_form>',views.Updateorderview,name='update'),

]