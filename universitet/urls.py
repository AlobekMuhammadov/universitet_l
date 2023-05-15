from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('yonalishlar/', ),
    path('fanlar/',fan),
    path('yonalishlar/',yonalish),
    path('yonalish_ochir/<int:son>/',yonalish_ochir),
    path('ustozlar/',ustoz),
    path('fan_ochir/<int:son>/',fan_ochir),
    path('ustoz_ochir/<int:son>/',ustoz_ochir),
]
