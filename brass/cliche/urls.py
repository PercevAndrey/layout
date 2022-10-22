from django.urls import path

from cliche.views import *


urlpatterns = [
    path('', run_index, name='home'),
]
