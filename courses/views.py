from django.shortcuts import render, redirect
from .models import Courses
from .forms import CourseFrom


# Create your views here.
def main(request):
    return render(request, 'courses/courses.html')


def courses(request):
    courses = Courses.objects.all()
    return render(request, 'courses/courses.html', context={'courses': courses})


def course(request, pk):
    courseObj = Courses.objects.get(id=pk)
    context = {'course': courseObj}
    return render(request, 'courses/single-course.html', context)


def createCourse(request):
    form = CourseFrom()

    if request.method == 'POST':
        form = CourseFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')

    context = {'form': form}
    return render(request, 'courses/course_form.html', context)


def editCourse(request, pk):
    courseObj = Courses.objects.get(pk=pk)
    form = CourseFrom(instance=courseObj)

    if request.method == 'POST':
        form = CourseFrom(request.POST, instance=courseObj)
        if form.is_valid():
            form.save()
            return redirect('cources')

    context = {'form': form, 'course': courseObj}
    return render(request, 'courses/course_form.html', context)


def deleteCourse(request, pk):
    courseObj = Courses.objects.get(id=pk)
    courseObj.delete()
    return redirect('cources')