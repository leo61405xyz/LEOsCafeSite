from django.shortcuts import render, redirect
from LEOsCafeSiteapp import models, forms
from LEOsCafeSiteapp.models import OrderItem, CoffeeBeanItem
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.
def index(request):
	CoffeeBeanItems = CoffeeBeanItem.objects.all().order_by('id')
	
	try:
		CoffeeBeanToday = CoffeeBeanItem.objects.filter(CBcoffeetoday='Yes').order_by('id')[0]
	except IndexError:
		CoffeeBeanToday = '無'

	return render(request, "index.html", locals())

def ordercafe(request):
    if request.method == "POST":  #如果是以POST方式才處理
        orderform = forms.OrderForm(request.POST)  #建立forms物件
        if orderform.is_valid():  #通過forms驗證
            name =  orderform.cleaned_data['boardname']
            temperature =  orderform.cleaned_data['boardtemperature']
            cupnumber =  orderform.cleaned_data['boardcupnumber']

            unit = models.OrderItem.objects.create(Oname=name, Otemperature=temperature, Ocupnumber=cupnumber)  #新增資料記錄
            unit.save()  #寫入資料庫

            message = '已儲存...'

            orderform = forms.OrderForm()
            return redirect('/index/')
        else:
            message = '驗證碼錯誤'
    else:
        message = ''
        orderform = forms.OrderForm()    
    return render(request, "ordercafe.html", locals())

def login(request):  #登入
	messages = ''  #初始時清除訊息
	if request.method == 'POST':  #如果是以POST方式才處理
		name = request.POST['username'].strip()  #取得輸入帳號
		password = request.POST['passwd']  #取得輸入密碼
		user1 = authenticate(username=name, password=password)  #驗證
		if user1 is not None:  #驗證通過
			if user1.is_active:  #帳號有效
				auth.login(request, user1)  #登入
				return redirect('/adminmain/')  #開啟管理頁面
			else:  #帳號無效
				message = '帳號尚未啟用！'
		else:  #驗證未通過
			message = '登入失敗！'
	return render(request, "login.html", locals())

def logout(request):  #登出
	auth.logout(request)
	return redirect('/index/')

def adminmain(request):
	CoffeeBeanItems = CoffeeBeanItem.objects.all().order_by('id')
	OrderItems = OrderItem.objects.all().order_by('Oodertime')
	return render(request, "adminmain.html", locals())

def orderview(request):
	OrderItems = OrderItem.objects.all().order_by('Oodertime')
	return render(request, "orderview.html", locals())

def cafeedit(request, cafeid=None, mode=None):
	#print(mode)
	if mode == 'load':
		CoffeeBeanUnit = models.CoffeeBeanItem.objects.get(id=cafeid)

		return render(request, "cafeedit.html", locals())

	elif mode == 'save':
		CoffeeBeanUnit = models.CoffeeBeanItem.objects.get(id=cafeid)
		CoffeeBeanUnit.CBname=request.POST['cb_name']
		CoffeeBeanUnit.CBcoffeeshop=request.POST['cb_coffeeshop']
		CoffeeBeanUnit.CBplace=request.POST['cb_place']
		CoffeeBeanUnit.CBroasting=request.POST['cb_roasting']
		CoffeeBeanUnit.CBprice=request.POST['cb_price']
		CoffeeBeanUnit.CBflavor=request.POST['cb_flavor']
		CoffeeBeanUnit.CBurl=request.POST['cb_url']
		CoffeeBeanUnit.CBcoffeetoday=request.POST['cb_coffeetoday']

		CoffeeBeanUnit.save()

		message = '已修改...'

		return redirect('/adminmain/')

def cafedelete(request, cafeid=None):
	if cafeid!=None:
		print(request.method)
		if request.method == "POST":  #如果是以POST方式才處理
			cafeid=request.POST['cafeid']
		try:
			CoffeeBeanUnit = models.CoffeeBeanItem.objects.get(id=cafeid)
			#print(CoffeeBeanUnit)
			CoffeeBeanUnit.delete()
			return redirect('/adminmain/')
		except:
			message = "讀取錯誤!"
			print(message)
	return render(request, "cafedelete.html", locals())

def cafeadd(request):
    if request.method == "POST":  #如果是以POST方式才處理
        addcafeform = forms.CafeForm(request.POST)  #建立forms物件
        if addcafeform.is_valid():  #通過forms驗證
            addcbname =  addcafeform.cleaned_data['boardcbname']
            addcbcoffeeshop = addcafeform.cleaned_data['boardcbcoffeeshop']
            addcbplace = addcafeform.cleaned_data['boardcbplace']
            addcbroasting = addcafeform.cleaned_data['boardcbroasting']
            addcbprice = addcafeform.cleaned_data['boardcbprice']
            addcbflavor = addcafeform.cleaned_data['boardcbflavor']
            addcburl = addcafeform.cleaned_data['boardcburl']
            addcbcoffeetoday = addcafeform.cleaned_data['boardcbcoffeetoday']

            unit = models.CoffeeBeanItem.objects.create(
				CBname=addcbname,
				CBcoffeeshop=addcbcoffeeshop,
				CBplace=addcbplace,
				CBroasting=addcbroasting,
				CBprice=addcbprice,
				CBflavor=addcbflavor,
				CBurl=addcburl,
				CBcoffeetoday=addcbcoffeetoday
			)	#新增資料記錄
            unit.save()  #寫入資料庫

            message = '已儲存...'

            addcafeform = forms.CafeForm()
            return redirect('/adminmain/')
        else:
            message = '驗證碼錯誤'
    else:
        message = ''
        addcafeform = forms.CafeForm()
    return render(request, "cafeadd.html", locals())

def orderdelete(request, orderid=None):
	if orderid!=None:
		print(request.method)
		if request.method == "POST":  #如果是以POST方式才處理
			orderid=request.POST['orderid']
			print(orderid)
		try:
			OrderItemUnit = models.OrderItem.objects.get(id=orderid)
			#print(OrderItemUnit)
			OrderItemUnit.delete()
			return redirect('/adminmain/')
		except:
			message = "讀取錯誤!"
			print(message)
	return render(request, "orderdelete.html", locals())

def orderedit(request, orderid=None, mode=None):
    # 1. 先抓出資料庫中的原始資料
    try:
        OrderUnit = models.OrderItem.objects.get(id=orderid)
    except models.OrderItem.DoesNotExist:
        return redirect('/adminmain/')

    if mode == 'load':
        # 2. 將資料庫數值填入 Form 的 initial 字典中
        initial_data = {
            'boardname': OrderUnit.Oname,
            'boardtemperature': OrderUnit.Otemperature,
            'boardcupnumber': OrderUnit.Ocupnumber,
        }
        # 3. 建立帶有初始值的表單
        orderform = forms.OrderForm(initial=initial_data)
        
        return render(request, "orderedit.html", locals())

    elif mode == 'save':
        if request.method == 'POST':
            # 這裡要傳入 POST 來的資料進行驗證
            orderform = forms.OrderForm(request.POST)
            if orderform.is_valid():
                # 更新資料庫物件
                OrderUnit.Oname = orderform.cleaned_data['boardname']
                OrderUnit.Otemperature = orderform.cleaned_data['boardtemperature']
                OrderUnit.Ocupnumber = orderform.cleaned_data['boardcupnumber']
                OrderUnit.save()
                return redirect('/adminmain/')
            else:
                # 如果驗證失敗（例如驗證碼錯誤），回到頁面並顯示錯誤
                message = "表單內容有誤，請檢查驗證碼。"
                return render(request, "orderedit.html", locals())