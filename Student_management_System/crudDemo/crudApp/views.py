from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# READ
def retrieve_view(request):
    students = Student.objects.all()
    return render(request, "crudApp/index.html", {"students": students})

# CREATE
def create_view(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/check/')

    return render(request, "crudApp/create.html", {"form": form})

# DELETE
def delete_view(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/check/')

# UPDATE
def update_view(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        print("POST DATA:", request.POST) 

    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('/check/')

    return render(request, "crudApp/update.html", {"form": form})