from unicodedata import name
from django.urls import path
from api.views import StudentListApiView


app_name = 'api'


urlpatterns = [
    path('list-students/', StudentListApiView.as_view(), name='list-students'),
]
