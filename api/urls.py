from django.urls import path
from api import views


app_name = 'api'


urlpatterns = [
    path('student-list/', views.StudentListApiView.as_view(), name='student-list'),
    path('student-create/', views.StudentCreateApiView.as_view(),
         name='student-create'),

]
