from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from myapp.models import ClassRoom, Student
from.forms import ClassRoomForm,StudentForm, StudentModelForm
class FirstView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "classbased/first.html")

    def post(self, request, *args, **kwargs):
        pass



class ClassRoomView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title" : "Classroom",
            "classrooms" : ClassRoom.objects.all()
        }
        return render(request, "classbased/classroom.html", context=context)
    def post(self, request, *args, **kwargs):
        name = request.POST.get("class_name")
        ClassRoom.objects.create(name=name)
        return redirect('classroom_view')

class ClassRoomTemplateView(TemplateView):
    template_name = "classbased/classroom.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title" : "Classroom",
            "classrooms" : ClassRoom.objects.all()
        })
        return context


class StudentListView(ListView):
    model = Student
    template_name = "classbased/home.html"
    context_object_name = "students"

class StudentDetailView(DetailView):
    model = Student
    template_name = "classbased/student_detail.html"




def classroom_form(request):
    if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            ClassRoom.objects.create(name=name)
        return redirect("classroom_form")
    context = {
        "title": "ClassRoom Form",
        "form": ClassRoomForm(),
        "classrooms" : ClassRoom.objects.all()
    }
    return render(request, "classbased/classroom_form.html", context=context)

def student_form(request):
    if request.method == ("POST"):
        form = StudentModelForm(request.POST)
        if form.is_valid():
            # name =form.cleaned_data.get("name")
            # age = form.cleaned_data.get("age")
            # department= form.cleaned_data.get("department")
            # Student.objects.create(name=name, age=age,department=department)
            form.save()
            return  redirect(student_form)
    context = {
        "title" : "Student",
        "form" : StudentModelForm(),
        "students" : Student.objects.all()
    }
    return render(request, "classbased/student_model_form.html", context=context)



def  student_model_form(request):
    if request.method == ("POST"):
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            age = form.cleaned_data.get("age")
            department = form.cleaned_data.get("department")
            Student.objects.create(name=name, age=age, department=department)
            return redirect(student_form)
    context = {
        "title": "Student",
        "form": StudentForm(),
        "students": Student.objects.all()
    }
    return render(request, "classbased/student_form.html", context=context)
