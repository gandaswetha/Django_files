from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'text':'swetha reddy','numbers':100,'name':'chaitu'}
    return render(request,'templates_app/index.html',context_dict)


def other(request):
    return render(request,'templates_app/other.html')

def relative(request):
    return render(request,'templates_app/relative.html')
