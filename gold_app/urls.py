from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('gold/<location>', views.process_money),
    path('reset', views.reset),
    path('store', views.store_data),
    path('check', views.check_result),
    # path('farm', views.farm),
    # path('cave', views.cave),
    # path('house', views.house),
    # path('casino', views.casino),
]