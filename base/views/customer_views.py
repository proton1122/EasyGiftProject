

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from base.models import Order
from base.models import Reciever
import json
from base.forms import CustomerRegisterForm


#Customer_Register

def CustomerRegisterView(request):
    order = Order.objects.filter(id = request.GET['id']).first()
    item = json.loads(order.items)
    print(item[0]['name'])
    print(item[0]['image'])
    order.name = item[0]['name']
    order.image = item[0]['image']
    form = CustomerRegisterForm()
    return render(request, 'pages/customer_register.html',{'order':order, 'form':form})


# Customer_Comfirm

def CustomerConfirmView(request):

    # POST処理の場合はifの中を実行
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST) # formで送信された値を取得
        if form.is_valid(): # フォームのバリデーション
            
            cd = form.cleaned_data
            customerData = Reciever(
                customer_name = cd['customer_name'],
                customer_zipcode = cd['customer_zipcode'],
                customer_prefecture = cd['customer_prefecture'],
                customer_city = cd['customer_city'],
                customer_address1 = cd['customer_address1'],
                customer_address2 = cd['customer_address2'],
                customer_tel = cd['customer_tel'],
                customer_mail = cd['customer_mail']
            )
            customerData.save()
            
            
            # form.save()
            # 値をそれぞれ取り出す
            # print("お名前: " + f['名前'])
            # print("メールアドレス: " + form.cleaned_data['メールアドレス'])
            # print("郵便番号: " + form.cleaned_data['郵便番号'])
            # return HttpResponseRedirect('/customer/confirm/')
            # return redirect('customer/confirm/')
    else:
        form = CustomerRegisterForm()
    
    return render(request, 'pages/customer_confirm.html', {'form': form})



 #Customer_Complete


def CustomerCompleteView(request):
 return render(request, 'pages/customer_complete.html')