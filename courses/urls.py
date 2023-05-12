from django.urls import path
from courses import views

urlpatterns = [
    path('', views.main, name='home'),
    path('courses/', views.courses, name='courses'),
    path('course/<str:pk>/', views.course, name='single-course'),
    path('create-course/', views.createCourse, name='create-course'),
    path('delete-course/<str:pk>', views.deleteCourse, name='delete-course'),
    path('edit-course/<str:pk>', views.editCourse, name='edit-course'),

]