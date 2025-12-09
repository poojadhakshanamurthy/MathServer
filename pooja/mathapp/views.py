from django.shortcuts import render
def efficiency(request):
    D=int(request.POST.get('distance_travelled',0))
    f=int(request.POST.get('fuel_consumed',0))
    m=D/f if request.method=='POST' else 0
    print("Distance travelled=",D)    
    print("Fuel consumed=",f)
    print("Mileage=",m)
    return render(request,'mathapp/math.html',{'D':D,'f':f,'m':m})
