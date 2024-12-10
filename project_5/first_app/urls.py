from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('about/',views.about, name='aboutpage'),
    path('form/',views.submit_form, name='submit_form'),
    path('django_form/',views.DjangoForm, name='django_form'),
    path('student_form/',views.StudentForm, name='student_form'),
    path('password/',views.passwordValidation, name='password'),
]