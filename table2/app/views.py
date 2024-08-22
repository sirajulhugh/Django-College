# views.py
from django.shortcuts import render, redirect
from .models import Course, Student

def add_course(request):
    return render(request,'add_course.html')

def page1(request):
    return render(request,'page1.html')

def add_student(request):
    a=Course.objects.all()
    return render(request,'add_student.html',{'courses':a})

def student_list(request):
    return render(request,'student_list.html')

# View to add courses
def addcourse(request):
    if request.method == 'POST':
        name = request.POST['name']
        fee = request.POST['fee']
        Course.objects.create(name=name, fee=fee)
        return redirect('add_student')
    return render(request, 'add_course.html')

# View to add students
def addstudent(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        date_of_join = request.POST['date_of_join']
        course_id = request.POST['course']
        course = Course.objects.get(id=course_id)
        #Student.objects.create(name=name, age=age, address=address, date_of_join=date_of_join, course=course)
        std=Student(name=name, age=age, address=address, date_of_join=date_of_join, course=course)
        std.save()
    return redirect('student_list')
    

# View to display students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def edit_page(request,id):
    std=Student.objects.get(id=id)
    cou=Course.objects.all()
    return render(request,"edit_page.html",{'student':std,'course':cou})

def update(request,id):
    if request.method == 'POST':
        std=Student.objects.get(id=id)
        std.name = request.POST['name']
        std.age = request.POST['age']
        std.address = request.POST['address']
        std.date_of_join = request.POST['date_of_join']
        cor=request.POST['course']
        cor1=Course.objects.get(id=cor)
        cor1.save()
        std.course=cor1
        std.save()
        return redirect('student_list')

def delete(request,id):
    std=Student.objects.get(id=id)
    std.delete()
    return redirect('student_list')
    
    

        
    


