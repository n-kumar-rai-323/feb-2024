from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Student
# Create your views here.

def hello_world(request):
    return JsonResponse({
        "message" : "hello World"
    })


class UserView(APIView):
    def get(self,*args,**kwargs):
        return Response({
           "name" : "jon snow",
            "age" : 34,
            "address" : "Sindhuli"
        })
class UserListView(APIView):
    def get(self,*args,**kwargs):
        users =[
            {"name": "jon show", "age": 23},
            {"name": "jon show", "age": 23},
            {"name": "jon show", "age": 23},

        ]
        return Response(users)
class StudentView(APIView):
    def get(self,request, *args, **kwargs):
        student = Student.objects.get(id=8)
        return Response({
            "name" : student.name,
            "age" : student.age,
            "department" : student.department,
            "classroom" : student.classroom.name
        })


class StudentListView(APIView):
    def get(self,request,*args, **kwargs):
        students_list = []
        for student in Student.objects.all():
            student = {
                "name" : student.name,
                "age": student.age,
                "department": student.department,
                "classroom":student.classroom.name if student.classroom else None
            }
            students_list.append(student)
        return Response(students_list)