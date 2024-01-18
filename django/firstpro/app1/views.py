
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import StudentDetail
import datetime


# Create your views here.

def test_view(request):
    return render(request, 'app1/index.html')


def test_view1(request):
  student = StudentDetail.objects.filter(is_delete=False)
  return render(request, 'app1/home.html',{'students':student})


def form_view(request):
    if request.method == "POST":
        error_msg = []
        email1 = request.POST['email']#request .POST.get('email')
        address1 = request.POST['address']
        phone_number1 = request.POST['phone_number']
        
        
        if len(phone_number1)!=10:
            error_msg.append("Mobile number should be 10 digit length.")

        if not email1:
            error_msg.append("Email can not blank.")  

        if not address1:
            error_msg.append("Addeess can not be blank.")  

        if StudentDetail.objects.filter(phone_number=phone_number1).exists():
            error_msg.append("Mobile Number already Exists.")
        if error_msg:
            messages.error(request, error_msg)
            return redirect('/form')       

        #syntax:model_name.objects.create(db_field_name=value, db_field_name =value) 
        user = User.objects.first()
        StudentDetail.objects.create(email=email1, address=address1, phone_number=phone_number1, 
                                        created_by = user, created_at=datetime.datetime.now())
        
                            
    return render(request, 'app1/form.html')


def edit_item(request, pk):
   student = StudentDetail.objects.get(Reference_id=pk) 
   if request.method == "POST":
       email1 = request.POST['email']#request .POST.get('email')
       address1 = request.POST['address']
       phone_number1 = request.POST['phone_number']
       StudentDetail.objects.filter(Reference_id=pk).update(email=email1, address= address1, phone_number=phone_number1)
       return redirect('/home')

   
      
      
   return render(request,'app1/edit.html',{'student':student})


def delete_item(request, pk):
   stu = StudentDetail.objects.get(Reference_id=pk)
   stu.is_delete=True
   stu.save()
   return redirect('/home')


