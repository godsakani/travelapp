from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import BusModel, CustomerModel , OrderModel
def adminloginview(request):
    return render(request,"travelapp/adminlogin.html")
def authenticateadmin(request):
    username=request.POST['username']
    password=request.POST['password']

    user = authenticate(username = username,password = password)

    #user exist
    if user is not None:
        login(request,user)
        return redirect('adminhomepage')
    #user does not exit
    if user is None:
       return redirect('adminloginpage')
def adminhomepageview(request):
    context = {'buses' : BusModel.objects.all()}
    return render(request,"travelapp/adminhomepage.html",context)
def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')
def addbus(request):
    #code to add bus in to the database
    name = request.POST['Bus']
    price = request.POST['price']
    BusModel(name = name, price = price).save()
    return redirect('adminhomepage')
    pass
def deletebus(request,busapk):
    BusModel.objects.filter(id = busapk).delete()
    return redirect('adminhomepage')
def homepageview(request):
    return render(request,"travelapp/homepage.html")
def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phoneno']
    #if username exist
    if User.objects.filter( username = username).exists():
        messages.add_message(request,messages.ERROR,"User Already exist")
        return redirect('homepage')
    #if username does not exist
    User.objects.create_user(username = username, password = password).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(userid = User.objects.all()[int(lastobject)].id, phoneno = phoneno).save()
    messages.add_message(request,messages.ERROR,"Account Created successful")
    return redirect('homepage')
def userloginview(request):
    return render(request,"travelapp/userlogin.html")
def userauthenticate(request):
    username=request.POST['username']
    password=request.POST['password']

    user = authenticate(username = username,password = password)

    #user exist
    if user is not None:
        login(request,user)
        return redirect('customerpage')
    #user does not exit
    if user is None:
       return redirect('userloginpage')
def customerwelcomeview(request):
    if not request.user.is_authenticated:
	    return redirect('userloginpage')
    username = request.user.username
    context = {'username' : username, 'buses' : BusModel.objects.all()}
    return render(request,"travelapp/customerwelcome.html",context)
def userlogout(request):
    logout(request)
    return redirect('userloginpage')
def placeorder(request):
	if not request.user.is_authenticated:
		return redirect('userloginpage')

	username = request.user.username
	phoneno = CustomerModel.objects.filter(userid = request.user.id)[0].phoneno
	address = request.POST['address']
	ordereditems = ""
	for bus in BusModel.objects.all():
		busid = bus.id
		name = bus.name
		price = bus.price

		quantity = request.POST.get(str(busid)," ")




		if str(quantity)!="0" and str(quantity)!=" ":
			ordereditems = ordereditems + name+" " + "price : " + str(int(quantity)*int(price)) +" "+ "quantity : "+ quantity+"    "

	print(ordereditems)

	OrderModel(username = username,phoneno = phoneno,address = address,ordereditems = ordereditems).save()
	messages.add_message(request,messages.ERROR,"order succesfully placed")
	return redirect('customerpage')
def userorders(request):
    orders = OrderModel.objects.filter(username = request.user.username)
    context = {'orders': orders}
    return render(request,'travelapp/userorders.html',context)
def adminorders(request):
    orders = OrderModel.objects.all()
    context = {'orders': orders}
    return render(request,'travelapp/adminorders.html',context)
def acceptorder(request,orderpk):
    order=OrderModel.objects.filter(id = orderpk)[0]
    order.status = "accepted"
    order.save()
    return  redirect(request.META['HTTP_REFERER'])
def declineorder(request,orderpk):
    order=OrderModel.objects.filter(id = orderpk)[0]
    order.status = "declined"
    order.save()
    return  redirect(request.META['HTTP_REFERER'])