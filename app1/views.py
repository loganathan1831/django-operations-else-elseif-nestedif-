from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':123,'b':4234,'c':3456}
    return render(request,'operations.html',d)