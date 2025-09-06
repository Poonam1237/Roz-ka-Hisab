from django.shortcuts import render,redirect
from .models import FamilyMembers,Expense
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method=='POST':
        n=request.POST.get('name')
        uname=n.capitalize()

        member=FamilyMembers.objects.filter(name=uname).first()
        if member:
            return redirect("member", mname=member.name)
        else:
            messages.error(request, "❌ Member Not Found!")
            # return redirect('AddNew')

    return render(request,'home.html')

def member(request,mname):
    m=FamilyMembers.objects.get(name=mname)
    if request.method=='POST':
        am=request.POST.get('amount')
        ca=request.POST.get('category')
        date=request.POST.get('date')
        time=request.POST.get('time')
        note=request.POST.get('note')

        MemberExpense=Expense.objects.filter(member=m)
        data={
            'member':m,
            'amount':am,
            'category':ca,
            'date':date,
            'time':time,
            'memberexpense':MemberExpense
        }
        e=Expense.objects.create(member=m,amount=am,category=ca,note=note)
        e.save()
        return render(request,'member.html',{'data':data})
      
    return render(request,'member.html')


# def delete(request,expid):
#     exp=Expense.objects.get(id=expid)
#     mname1=exp.member.name
#     exp.delete()
#     return redirect('member',mname=mname1)



def account(request,aname):
    member = FamilyMembers.objects.get(name=aname)
    
    exp=Expense.objects.filter(member=member)

    sum1 = sum(i.amount for i in exp)
    return render(request,'account.html',{'details':exp,'sum1':sum1})


def about(request):
    return render(request,'about.html')

def dashboard(request):
  
    members = FamilyMembers.objects.all()
    fl = []
    totals = []

    for m in members:
        s = 0
        expenses = Expense.objects.filter(member=m)
        for exp in expenses:  
            s += exp.amount
        totals.append(s)
        fl.append((m, s)) 

    fs = sum(totals)
    return render(request, 'dashboard.html', {'fl': fl, 'fs': fs})