from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def studentreg(request):
    return render(request,'studentreg.html')

def studentdetails(request):
    if request.method == 'POST':
        studentname = request.POST.get('sname')
        addr=request.POST.get('address')
        age=request.POST.get('age')
        email=request.POST.get('email')
        date=request.POST.get('date')
        qual=request.POST.get('qualification')
        gender=request.POST.get('gender')
        contact=request.POST.get('contact')
        obj=Student(Name=studentname, address=addr,age=age,email=email,joinIngdate=date,qualification=qual,gender=gender,mobileno=contact)
        obj.save()
        return redirect('showstudentdetails')
    
def showstudentdetails(request):
    stu=Student.objects.all()
    return render(request, 'studentdetails.html', {'student':stu})

def editdetails(request,id):
    sobj=Student.objects.get(id=id)
    return render(request, 'edit.html',{'s':sobj})

def editpage(request,id):
    if request.method == 'POST':
        student=Student.objects.get(id=id)
        student.Name=request.POST.get('sname')
        student.address=request.POST.get('address')
        student.age=request.POST.get('age')
        student.email=request.POST.get('email')
        student.joinIngdate=request.POST.get('date')
        student.qualification=request.POST.get('qualification')
        student.gender=request.POST.get('gender')
        student.mobileno=request.POST.get('contact')
        student.save()
        return redirect('showstudentdetails')
    return render(request,'edit.html')

def deletepage(request,id):
    S=Student.objects.get(id=id)
    S.delete()
    return redirect('showstudentdetails')

def viewpage(request,id):
    view=Student.objects.get(id=id)
    return render(request,'view.html',{"details":view})