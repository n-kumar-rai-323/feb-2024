from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,JsonResponse
from .models import Student,ClassRoom,StudentProfile
# Create your views here.
def home(request):
    return render(request, "myapp/home.html")


def index(request):
    context = {"students": Student.objects.all(), "title":"Student"}
    return render(request, template_name="myapp/index.html", context=context)



def view_name_jon(request):
    return render(request, "myapp/jon.html")

def view_name_jane(request):
    return render(request, "myapp/jane.html")
def view_name(request, name):
    last_name = request.GET.get('last_name')
    print(last_name)
    if name.lower() == 'ram':
        full_name= "Ram bahadur"
    elif name.lower() == 'harry':
        full_name = "Harry Krishna"
    elif name.lower() == 'jon':
        full_name = "jon prasad"
    else:
        return HttpResponseNotFound("<h1> Name not found</h1>")
    context = {
        "name" : full_name,
    }
    if last_name:
        context.update(last_name=last_name)

    return render(request, "myapp/name.html", context= context)


def json_view(request):
    # response = {"id": 1, "name" : "nishan", "age" : 25}
    students=[
        {"id":1, "name": "ken", "age": 25},
        {"id": 1, "name": "ken", "age": 25},
        {"id":1, "name": "ken", "age": 25},
        {"id": 1, "name": "ken", "age": 25},


    ]
    return JsonResponse(students, safe=False)




# def index(request):
#     context = {"id":1, "name" : "Nishan" , "age": 25, "title": "student"}
#     return render(request, template_name="myapp/index.html", context = context)




def students(request):
    context = {
        "title":"Students",
        "classrooms" : ClassRoom.objects.all(),
        "students":Student.objects.all(),
        "st":StudentProfile.objects.all()
    }

    return render(request, "myapp/students.html", context=context)



def page1(request):
    return render(request, "myapp/page1.html")





def  student_detail(request, id):
    context ={
        "student" :Student.objects.get(id=id),
        "title" : "Student Detail"

    }
    return render(request, "myapp/student_detail.html", context=context)
