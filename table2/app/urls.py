# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_course, name='add_course'),
    path('addstudent', views.add_student, name='add_student'),
    path('studentlist', views.student_list, name='student_list'),
    path('addcou', views.addcourse, name='addcourse'),
    path('addstu', views.addstudent, name='addstudent'),
    path('edit_page/<int:id>', views.edit_page, name='edit_page'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('page1', views.page1, name='page1'),

    
]
