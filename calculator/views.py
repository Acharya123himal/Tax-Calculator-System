from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth import get_user_model
from .models import TaxCalculator
from .forms import CalculatorForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

user = get_user_model()

def tax_calculation(salary,tax,record,marital_status):
    if marital_status=='unmarried':
        if(salary>2000000):
            record['2000000']=[salary-2000000,36,0.36*(salary-2000000)]
            return tax_calculation(2000000,tax+0.36*(salary-2000000),record,marital_status)
        elif (salary>700000):
            record['700000']=[salary-700000,30,0.3*(salary-700000)]
            return tax_calculation(700000,tax+0.3*(salary-700000),record,marital_status)
        elif salary>(500000):
            record['500000']=[salary-500000,20,0.2*(salary-500000)]
            return tax_calculation(500000,tax+0.2*(salary-500000),record,marital_status)
        elif salary>(400000):
            record['400000']=[salary-400000,10,0.1*(salary-400000)]
            return tax_calculation(400000,tax+0.1*(salary-400000),record,marital_status)
        else:
            record['0']=[salary,1,0.01*(salary)]
            return [tax+0.01*salary,record]
    else:
        if(salary>2000000):
            record['2000000']=[salary-2000000,36,0.36*(salary-2000000)]
            return tax_calculation(2000000,tax+0.36*(salary-2000000),record,marital_status)
        elif (salary>750000):
            record['750000']=[salary-750000,30,0.3*(salary-750000)]
            return tax_calculation(750000,tax+0.3*(salary-750000),record,marital_status)
        elif salary>(550000):
            record['550000']=[salary-550000,20,0.2*(salary-550000)]
            return tax_calculation(550000,tax+0.2*(salary-550000),record,marital_status)
        elif salary>(450000):
            record['450000']=[salary-450000,10,0.1*(salary-450000)]
            return tax_calculation(450000,tax+0.1*(salary-450000),record,marital_status)
        else:
            record['0']=[salary,1,0.01*(salary)]
            return [tax+0.01*salary,record]

@cache_control(no_cache=True, must_revalidate=True)
def calculator(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        marital_status=request.POST.get('marital-status')
        age=int(request.POST.get('age'))
        fiscal_year=request.POST.get('fiscal-year')
        monthly_salary=int(request.POST.get('monthly-salary'))
        months=int(request.POST.get('months'))
        bonus=int(request.POST.get('bonus'))
        allowance=int(request.POST.get('allowance'))
        others=int(request.POST.get('others'))
        epf=int(request.POST.get('employee-provident-fund'))
        cit=int(request.POST.get('citizen-investment-trust'))
        sum_epf_cit=epf+cit
        insurance=int(request.POST.get('insurance'))
        medical_expense=int(request.POST.get('medical-expense'))
        medical_tax=0.15*medical_expense
        other_expense=int(request.POST.get('other_expense'))
        annual_salary=monthly_salary*months+bonus+allowance+others
        total_deduction=sum_epf_cit+insurance+medical_expense+other_expense
        net_accessable=annual_salary-total_deduction
        annual_tax_record=tax_calculation(net_accessable,0,{},marital_status)
        annual_tax=annual_tax_record[0]
        record=annual_tax_record[1]
        liable_tax=annual_tax-medical_tax
        liable_tax_monthly=int(liable_tax/12)
        data={
            'name':name,
            'address':address,
            'annual_salary':annual_salary,
            'annual_tax':annual_tax,
            'sum_epf_cit':sum_epf_cit,
            'insurance':insurance,
            'total_deduction':total_deduction,
            'net_accessable':net_accessable,
            'record':record,
            'medical_tax':medical_tax,
            'liable_tax':liable_tax,
            'liable_tax_monthly':liable_tax_monthly
        }
        return render(request,'result.html',data)
    else:
        return render(request, 'calculation.html',)
    
@login_required(login_url = "login")
def history(request):
    if request.method == 'GET':
        tax = TaxCalculator.objects.filter(email = request.user.email)
        print(tax)
        return render(request,"history.html",{"tax":tax,})


@login_required(login_url = "login")
def save_calculation(request):
    form = CalculatorForm(request.GET or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.email = request.user.email
        record.save()
        messages.success(request,"Saved Successfully")
        return HttpResponseRedirect("/dashboard")
    return HttpResponseRedirect('/calculator')