from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('home',views.index,name='home'),
    path('predict',views.predict,name='predict'),
    # path('report',views.report,name='report')
]