from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.contrib import messages
from mainApp.forms import *
from mainApp.models import *
from django.utils.timezone import datetime as forProfitDateTime 
import datetime

# Create your views here.
def index(request):
    user_in=False
    emp_in=False
    u_name= request.user.username
    emp_status = emp_register.objects.filter(e_name=u_name,available=True)
    registered_user_data = user_register.objects.filter(u_name=u_name)
    if registered_user_data:
        user_in=True

    registered_emp_data = emp_register.objects.filter(e_name=u_name)
    if registered_emp_data:
        emp_in=True
    
    return render(request, 'main.html',{'user_in1':user_in,'emp_in1':emp_in,'u_name':u_name,'emp_status1':emp_status})
def userRegister(request):
    u_name=request.user.username
    f1=f_user_register(request.POST or None)
    if f1.is_valid():
        f1.save()
        messages.success(request, 'Hello %s!! User registration completed successfully.'% u_name)
        messages.success(request, 'Your phone number is set as Whatsapp number. You can change it later from the "My Profile" option.')
        addWhatsappNumber(request)
        return redirect('mainApp1:index1')
    return render(request,'user_register.html',{'form':f1,'u_name':u_name})
def addWhatsappNumber(request):
    u_name=request.user.username
    phone_number = user_register.objects.filter(u_name=u_name)
    if phone_number:
        phone_number = phone_number[0].phone_number
        user_register.objects.filter(u_name=u_name).update(whatsapp_number=phone_number)

def searchWorkers(request):
    user_in=False
    emp_in=False
    u_name= request.user.username
    emp_status = emp_register.objects.filter(e_name=u_name,available=True)
    register_data = user_register.objects.filter(u_name=u_name)
    if register_data:
        user_in=True
    registered_emp_data = emp_register.objects.filter(e_name=u_name)
    if registered_emp_data:
        emp_in=True
    
    searched_trade = request.GET.get('trade_name')
    searched_location = request.GET.get('location_name')

    if searched_trade and searched_location:
        workers_data1 = emp_register.objects.filter(service_name=searched_trade,location=searched_location,available=True)
        workers_data2 = emp_register.objects.filter(service_name=searched_trade,location=searched_location,available=False)
        based_on = 'both'
        return render(request,'search_workers.html',{'user_in1':user_in,'workers_data1':workers_data1,'workers_data2':workers_data2,'based_on1':based_on,'u_name':u_name,'emp_status1':emp_status})
    elif searched_trade:
        workers_data1 = emp_register.objects.filter(service_name=searched_trade,available=True)
        workers_data2 = emp_register.objects.filter(service_name=searched_trade,available=False)
        based_on = 'trade'
        return render(request,'search_workers.html',{'user_in1':user_in,'workers_data1':workers_data1,'workers_data2':workers_data2,'based_on1':based_on,'u_name':u_name,'emp_status1':emp_status})
    elif searched_location:
        workers_data1 = emp_register.objects.filter(location=searched_location,available=True)
        workers_data2 = emp_register.objects.filter(location=searched_location,available=False)
        based_on = 'location'
        return render(request,'search_workers.html',{'user_in1':user_in,'workers_data1':workers_data1,'workers_data2':workers_data2,'based_on1':based_on,'u_name':u_name,'emp_status1':emp_status})
    else:
        workers_data1 = emp_register.objects.filter(available=True)
        workers_data2 = emp_register.objects.filter(available=False)
        return render(request,'search_workers.html',{'user_in1':user_in,'workers_data1':workers_data1,'workers_data2':workers_data2,'u_name':u_name,'emp_status1':emp_status})

def empRegister(request):
    e_name=request.user.username
    f1=f_emp_register(request.POST or None, request.FILES)
    if f1.is_valid():
        f1.save()
        messages.success(request, 'Hello %s!! Employee registration completed successfully.'% e_name)
        return redirect('mainApp1:index1')
    return render(request,'emp_register.html',{'form':f1,'e_name':e_name})

def toggleStatus(request):
    u_name= request.user.username
    emp_status = emp_register.objects.filter(e_name=u_name).values('available')
    limitations = services.objects.filter(Q(e_name=u_name,accepted=True)|Q(e_name=u_name,working=True)|Q(e_name=u_name,confirm_working=True))
    
    if emp_status[0]['available'] == 0 and not limitations:
        emp_register.objects.filter(e_name=u_name).update(available=1)
    else:
        emp_register.objects.filter(e_name=u_name).update(available=0)
    return redirect('../')

def empProfileByUser(request,e_name):
    user_in=False
    emp_in=False
    u_name= request.user.username
    emp_status = emp_register.objects.filter(e_name=u_name,available=True)

    register_data = user_register.objects.filter(u_name=u_name)
    if register_data:
        user_in=True
    registered_emp_data = emp_register.objects.filter(e_name=u_name)
    if registered_emp_data:
        emp_in=True
    emp_data = emp_register.objects.filter(e_name=e_name).all()

    accepted_count = services.objects.filter(e_name=e_name,paid=1).count()
    completed_count = services.objects.filter(e_name=e_name,completed=1).count()
    liked_count = services.objects.filter(e_name=e_name,feedback=1).count()
    unliked_count = services.objects.filter(e_name=e_name,feedback=0).count()

    return render(request, 'emp_profile_by_user.html',{
        'user_in1':user_in,
        'emp_in1':emp_in,
        'emp_data1':emp_data,
        'u_name':u_name,
        'emp_status1':emp_status,
        'accepted_count1':accepted_count,
        'completed_count1':completed_count,
        'liked_count1':liked_count,
        'unliked_count1':unliked_count,
        })
def empProfile(request):
    user_in=False
    emp_in=False
    u_name= request.user.username
    e_name= request.user.username

    emp_status = emp_register.objects.filter(e_name=e_name,available=True)

    register_data = user_register.objects.filter(u_name=u_name)
    if register_data:
        user_in=True
    registered_emp_data = emp_register.objects.filter(e_name=e_name)
    if registered_emp_data:
        emp_in=True
    emp_data = emp_register.objects.filter(e_name=e_name).all()

    received_count = services.objects.filter(e_name=e_name).count()
    accepted_count = services.objects.filter(e_name=e_name,paid=1).count()
    rejected_count = services.objects.filter(e_name=e_name,rejected=1).count()
    completed_count = services.objects.filter(e_name=e_name,completed=1).count()
    incompleted_count = services.objects.filter(e_name=e_name,cancelled=1).count()
    liked_count = services.objects.filter(e_name=e_name,feedback=1).count()
    unliked_count = services.objects.filter(e_name=e_name,feedback=0).count()
    
    return render(request, 'emp_profile.html',{
        'user_in1':user_in,
        'emp_in1':emp_in,
        'emp_data1':emp_data,
        'u_name':u_name,
        'emp_status1':emp_status,
        'received_count1':received_count,
        'accepted_count1':accepted_count,
        'rejected_count1':rejected_count,
        'completed_count1':completed_count,
        'incompleted_count1':incompleted_count,
        'liked_count1':liked_count,
        'unliked_count1':unliked_count
        })
def empProfileEdit(request,phone):
    emp_in=False
    u_name= request.user.username
    emp_status = emp_register.objects.filter(e_name=u_name,available=True)
    registered_emp_data = emp_register.objects.filter(e_name=u_name)
    if registered_emp_data:
        emp_in=True

    instance = get_object_or_404(emp_register,phone_number=phone)
    t1 = f_emp_register_for_update(request.POST or None, request.FILES or None,instance=instance)
    if t1.is_valid():
        t1.save()
        return redirect('../')
    return render(request,'emp_profile_edit.html',{'form':t1,'emp_in1':emp_in,'u_name':u_name,'emp_status1':emp_status})

def userProfileEdit(request,phone):
    user_in=False
    u_name= request.user.username
    register_data = user_register.objects.filter(u_name=u_name)
    if register_data:
        user_in=True    

    instance = get_object_or_404(user_register,phone_number=phone)
    t1 = f_user_register_for_update(request.POST or None,instance=instance)
    if t1.is_valid():
        t1.save()
        # messages.info(request,'User Profile UPDATED Successfuly.')
        return redirect('../')
    return render(request,'user_profile_edit.html',{'form':t1,'user_in1':user_in,'u_name':u_name})

def userPageByAdmin(request):
    u_name= request.user.username
    searched_user_name = request.GET.get('user_name')
    if searched_user_name:
        user_data = user_register.objects.filter(u_name=searched_user_name)
        if not user_data:
            user_data = user_register.objects.filter(u_name=searched_user_name.lower())
        if not user_data:
            user_data = user_register.objects.filter(u_name=searched_user_name.upper())
        if not user_data:
            user_data = user_register.objects.filter(u_name=searched_user_name.title())
        if not user_data:
            user_data = user_register.objects.filter(u_name__startswith=str(searched_user_name)[0])
    else:
        user_data = user_register.objects.all()
    return render(request,'user_page_by_admin.html',{'user_data1':user_data,'u_name':u_name})

def userProfileByEmp(request,uname):
    emp_in = False
    ename= request.user.username
    user_data = user_register.objects.filter(u_name=uname)
    emp_status = emp_register.objects.filter(e_name=ename,available=True)

    register_data = emp_register.objects.filter(e_name=ename)
    if register_data:
        emp_in=True
    return render(request,'user_profile_by_emp.html',{'user_data1':user_data,'u_name':ename,'emp_in1':emp_in,'emp_status1':emp_status})

def userProfile(request):
    user_in = False
    u_name= request.user.username
    user_data = user_register.objects.filter(u_name=u_name)

    register_data = user_register.objects.filter(u_name=u_name)
    if register_data:
        user_in=True
    return render(request,'user_profile.html',{'user_data1':user_data,'u_name':u_name,'user_in1':user_in})

def serviceHistory(request):
    user_in=False
    emp_in=False
    u_name= request.user.username
    emp_status = emp_register.objects.filter(e_name=u_name,available=True)
    registered_user_data = user_register.objects.filter(u_name=u_name)
    if registered_user_data:
        user_in=True
    registered_emp_data = emp_register.objects.filter(e_name=u_name)
    if registered_emp_data:
        emp_in=True

    if emp_in:
        history_data = services.objects.filter(Q(e_name=u_name,cancelled=True)|Q(e_name=u_name,completed=True)|Q(e_name=u_name,rejected=True)).order_by('-end_date')
    else:
        history_data = services.objects.filter(Q(u_name=u_name,cancelled=True)|Q(u_name=u_name,completed=True)|Q(u_name=u_name,rejected=True)).order_by('-end_date')

    return render(request,'service_history.html',{'u_name':u_name,'emp_in1':emp_in,'user_in1':user_in,'emp_status1':emp_status,'history_data1':history_data})

def employeeHistoryByUser(request,e_name):
    user_in=False
    emp_in=False
    u_name= request.user.username
    emp_status = emp_register.objects.filter(e_name=u_name,available=True)
    registered_user_data = user_register.objects.filter(u_name=u_name)
    if registered_user_data:
        user_in=True

    registered_emp_data = emp_register.objects.filter(e_name=u_name)
    if registered_emp_data:
        emp_in=True    

    history_data = services.objects.filter(Q(e_name=e_name,cancelled=True)|Q(e_name=e_name,completed=True)|Q(e_name=e_name,rejected=True))

    history_data = history_data[::-1]   #Reversing the list( Recent Completion data First)
    return render(request,'employee_history_by_user.html',{'u_name':u_name,'e_name1':e_name,'emp_in1':emp_in,'user_in1':user_in,'history_data1':history_data})

def userHistoryByAdmin(request,uname):
    user_in=False
    emp_in=False
    u_name= request.user.username
    emp_status = emp_register.objects.filter(e_name=u_name,available=True)
    registered_user_data = user_register.objects.filter(u_name=u_name)
    if registered_user_data:
        user_in=True

    registered_emp_data = emp_register.objects.filter(e_name=u_name)
    if registered_emp_data:
        emp_in=True    

    history_data = services.objects.filter(Q(u_name=uname,cancelled=True)|Q(u_name=uname,completed=True)|Q(u_name=uname,rejected=True))

    history_data = history_data[::-1]   #Reversing the list( Recent Completion data First)
    return render(request,'user_history_by_admin.html',{'u_name':u_name,'emp_in1':emp_in,'user_in1':user_in,'history_data1':history_data})

def profit(request,based):
    is_emp = ''
    u_name = request.user.username 

    today = forProfitDateTime.today()
        # ALL
    if based == 'all':
            received_count = services.objects.all().count()
            paid_count = services.objects.filter(paid=1).count()
            rejected_count = services.objects.filter(rejected=1).count()
        # TODAY
    elif based == 'today':
            received_count = services.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day).count()
            paid_count = services.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day,paid=1).count()
            rejected_count = services.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day,rejected=1).count()
        # MONTH
    elif based == 'month':
            received_count = services.objects.filter(date__year=today.year, date__month=today.month).count()
            paid_count = services.objects.filter(date__year=today.year, date__month=today.month,paid=1).count()
            rejected_count = services.objects.filter(date__year=today.year, date__month=today.month,rejected=1).count()
        # YEAR
    elif based == 'year':
            received_count = services.objects.filter(date__year=today.year).count()
            paid_count = services.objects.filter(date__year=today.year,paid=1).count()
            rejected_count = services.objects.filter(date__year=today.year,rejected=1).count()
    else:
            is_emp = based
            received_count = services.objects.filter(e_name=based).count()
            paid_count = services.objects.filter(e_name=based,paid=1).count()
            rejected_count = services.objects.filter(e_name=based,rejected=1).count()

    pending_count = received_count-(paid_count+rejected_count)
    total = paid_count * 5 # 5 rupees per request
     # %
    if received_count != 0:
        paid_perc = (paid_count/received_count)*100
        rejected_perc = (rejected_count/received_count)*100
        pending_perc = 100-(paid_perc+rejected_perc)
    else:
        paid_perc = 0
        rejected_perc = 0
        pending_perc = 0

    return render(request,'profit.html',{
        'u_name':u_name,
        'is_emp1':is_emp,
        'received_count1':received_count,
        'paid_count1':paid_count,
        'rejected_count1':rejected_count,
        'pending_count1':pending_count,
        'paid_perc1':round(paid_perc),
        'rejected_perc1':round(rejected_perc),
        'pending_perc1':round(pending_perc),
        'total1':total,
        'based1':based
        })

def scheduledServices(request):
    user_in=False
    emp_in=False
    u_name= request.user.username
    e_name= request.user.username

    emp_status = emp_register.objects.filter(e_name=u_name,available=True)
    registered_user_data = user_register.objects.filter(u_name=u_name)
    if registered_user_data:
        user_in=True

    registered_emp_data = emp_register.objects.filter(e_name=u_name)
    if registered_emp_data:
        emp_in=True  

    user_service_data = services.objects.filter(u_name=u_name,rejected=0,cancelled=0,feedback='') 
    user_service_data = user_service_data[::-1]   #Reversing the list( Recent Completion data First)

    emp_service_data = services.objects.filter(e_name=e_name,rejected=0,completed=0,cancelled=0) 
    emp_service_data = emp_service_data[::-1]   #Reversing the list( Recent Completion data First)

    return render(request,'scheduled_services.html',{
        'u_name':u_name,
        'emp_status1':emp_status,
        'emp_in1':emp_in,
        'user_in1':user_in,
        'user_service_data1':user_service_data,
        'emp_service_data1':emp_service_data
        })

def confirmRequest(request,e_name):
    u_name= request.user.username
    emp_data = emp_register.objects.filter(e_name=e_name)
    for i in emp_data:
       services.objects.create(u_name=u_name,e_name=i.e_name,service_name=emp_data[0].get_service_name_display(),requested=True)
    return redirect('mainApp1:scheduledServices1')

def payAndAccept(request,id):
    services.objects.filter(id=id).update(requested=0,paid=1,accepted=1)
    #change availability status of employee
    toggleStatus(request) 
    #delete remaining requests of the same employee
    ename = services.objects.filter(id=id).values('e_name')[0]['e_name']
    services.objects.filter(e_name=ename,requested=1).delete()
    #delete remaining requests of user with same service name
    uname = services.objects.filter(id=id).values('u_name')[0]['u_name']
    service_name = services.objects.filter(id=id).values('service_name')[0]['service_name']
    services.objects.filter(u_name=uname,requested=1,service_name=service_name).delete()
    return redirect('mainApp1:scheduledServices1')

def reject(request,id):
    services.objects.filter(id=id).update(requested=0,working=0,rejected=1,end_date=datetime.datetime.now())
    return redirect('mainApp1:user_empServiceHistory1_BysScheduledServices')

def cancel(request,id):
    services.objects.filter(id=id).update(requested=0,working=0,cancelled=1,end_date=datetime.datetime.now())
    return redirect('mainApp1:user_empServiceHistory1_BysScheduledServices')

def startWorking(request,id):
    services.objects.filter(id=id).update(working=1,accepted=0)
    return redirect('mainApp1:scheduledServices1')

def confirmWorking(request,id):
    services.objects.filter(id=id).update(working=0,confirm_working=1)
    return redirect('mainApp1:scheduledServices1')

def completed(request,id):
    services.objects.filter(id=id).update(working=0,confirm_working=0,completed=1,end_date=datetime.datetime.now())
    toggleStatus(request)
    return redirect('mainApp1:user_empServiceHistory1_BysScheduledServices')

def neg_feedback(request,id):
    services.objects.filter(id=id).update(feedback=0)
    return redirect('mainApp1:user_empServiceHistory1_BysScheduledServices')
def pos_feedback(request,id):
    services.objects.filter(id=id).update(feedback=1)
    return redirect('mainApp1:user_empServiceHistory1_BysScheduledServices')
def promote(request,ename):
    emp_register.objects.filter(e_name=ename).update(verified=1)
    return redirect('mainApp1:searchWorkers1')
def demote(request,ename):
    emp_register.objects.filter(e_name=ename).update(verified=0)
    return redirect('mainApp1:searchWorkers1')
