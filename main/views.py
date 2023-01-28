from django.shortcuts import render , redirect
from main.models import Student
# Create your views here.
def home(request):
    return render(request,'Home.html')

def search(request):
    query = request.GET.get('query' , None)
    if query:
        results = Student.objects.filter(id__icontains=query)
        return render(request, 'Search.html', {'results': results})
    return render(request, 'Search.html', {})

def Department(request):
    return render(request,'Department.html')

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('student_id')
        gpa = request.POST.get('gpa')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        level = request.POST.get('level')
        Department = request.POST.get('Department')
        mobile = request.POST.get('mobile')
        status = request.POST.get('status')
        if student_id in Student.objects.all():
            return render(request, 'add.html')

        student = Student(name = name, id=student_id, GPA=gpa,  address=address, Date=date_of_birth, email=email, Gender=gender, level=level , department= Department , mobile_number= mobile, Status = status)
        student.save()
        return redirect('add')
    else:
        return render(request, 'add.html')

def Edit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('student_id')
        gpa = request.POST.get('gpa')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        level = request.POST.get('level')
        status = request.POST.get('status')
        Department = request.POST.get('Department')

        student = Student.objects.get(Student.objects.filter(id__icontains=student_id))
        student.name= name
        student.GPA = gpa
        student.Date=date_of_birth
        student.email = email
        student.Gender = gender
        student.level = level
        student.address = "123 st"
        student.Status = status 
        student.department = Department
        student.save()
        return redirect('add')
    else:
        return render(request, 'Edit.html')

def ViewAll(request):
    return render(request,'ViewAll.html' , {'students':Student.objects.all()})

   

   