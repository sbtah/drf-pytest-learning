from django.urls import path
from api import views


app_name = 'api'


urlpatterns = [
    path('student-list/', views.StudentListApiView.as_view(),
         name='student-list'),
    path('student-create/', views.StudentCreateApiView.as_view(),
         name='student-create'),
    path('student-details/<int:pk>/', views.StudentDetailsApiView.as_view(),
         name='student-details'),
    path('student-delete/<int:pk>/', views.StudentDeleteApiView.as_view(),
         name='student-delete'),
]
