from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'welcome.html')

# def showImg(request):
#     return  render(request,'demo.html')
#
# def ahmedabad(request):
#     return render(request,'ahmedabad.html')
#
# def gandhinagar(request):
#     return render(request,'gandhinagar.html')
#
# def rajkot(request):
#     return render(request,'rajkot.html')
#
# def surat(request):
#     return render(request,'surat.html')

def india(request):
    return  render(request,'india.html')

def uk(request):
    return  render(request,'uk.html')

def usa(request):
    return  render(request,'usa.html')

def argentina(request):
    return  render(request,'argentina.html')

def brazil(request):
    return  render(request,'brazil.html')

def germany(request):
    return  render(request,'germany.html')

def russia(request):
    return  render(request,'russia.html')