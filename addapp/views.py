from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Register
def reg(request):
	return render(request,"addapp/reg.html")
def reglogic(request):
	obj = Register(emailid=request.POST["txtemail"],password=request.POST["txtpass"],mobile=request.POST["txtmobile"],fullname=request.POST["txtname"])
	obj.save()
	return render(request,"addapp/reg.html",{'msg':'registration successfully'})
def viewreg(request):
	res = Register.objects.all()
	return render(request,"addapp/viewreg.html",{'res1':res})
def editreg(request):
	res = Register.objects.get(pk=request.GET["q"])
	return render(request,"addapp/editreg.html",{'res1':res})
def updatereg(request):
	res = Register.objects.get(pk=request.POST["txtid"])
	res.emailid=request.POST["txtemail"]
	res.password=request.POST["txtpass"]
	res.mobile=request.POST["txtmobile"]
	res.fullname=request.POST["txtfname"]
	res.save()
	return redirect('viewreg')
def deletereg(request):
	res = Register.objects.get(pk=request.GET["q"])
	return render(request,"addapp/deletereg.html",{'res1':res})
def deletecreg(request):
	res = Register.objects.get(pk=request.POST["txtid"])
	res.delete()
	return redirect('viewreg')
def index(request):
	return render(request,"addapp/index.html")
def addlogic(request):
	course   = request.POST.getlist('course[]')	 
	some_var = request.POST.getlist('checks[]')
	data1=''
	for data2 in course:
	    data1=data1+data2 +" "
	data=''
	for data3 in som_var:
	    data=data+data3 +" "	
	return HttpResponse("data is "+(data1+data))