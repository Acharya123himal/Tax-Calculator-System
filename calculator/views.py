from django.shortcuts import render
from django.http import HttpResponse

def tax_calculation(salary,tax,record):
    if(salary>2000000):
        record['2000000']=[salary-2000000,36,0.36*(salary-2000000)]
        return tax_calculation(2000000,tax+0.36*(salary-2000000),record)
    elif (salary>700000):
        record['700000']=[salary-700000,30,0.3*(salary-700000)]
        return tax_calculation(700000,tax+0.3*(salary-700000),record)
    elif salary>500000:
        record['500000']=[salary-500000,20,0.2*(salary-500000)]
        return tax_calculation(500000,tax+0.2*(salary-500000),record)
    elif salary>400000:
        record['400000']=[salary-400000,10,0.1*(salary-400000)]
        return tax_calculation(400000,tax+0.1*(salary-400000),record)
    else:
        record['0']=[salary,1,0.01*(salary)]
        return [tax+0.01*salary,record]

def calculator(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
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
        annual_tax_record=tax_calculation(net_accessable,0,{})
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
        return render(request, 'calculation.html')

