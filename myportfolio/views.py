from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'project.html')
def main(request):
    return render(request,'home.html')