from django.shortcuts import render
# from EduCart.EduCartApp.models import courses, Tutorials, Product


# Create your views here.


def c_tutorial(request):
    # tutorial = Tutorials.objects.all()  {'tutorial':tutorial}
    return render(request, 'Tutorials/C/c_tutorial.html')


def django_tutorial(request):
    return render(request, 'Tutorials/django_tutorial.html')


def java_tutorial(request):
    return render(request, 'Tutorials/java/java_tutorial.html')


def html_tutorial(request):
    return render(request, 'Tutorials/html_tutorial.html')


def css_tutorial(request):
    return render(request, 'Tutorials/css_tutorial.html')


def python_tutorial(request):
    return render(request, 'Tutorials/python_tutorial.html')


def android_tutorial(request):
    return render(request, 'Tutorials/android_tutorial.html')


