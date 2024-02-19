from django.urls import path
from .views import home,index,view_name_jon,view_name_jane,view_name,json_view,students,page1, student_detail

urlpatterns =[
    path("name/jon/", view_name_jon),
    path("name/jane", view_name_jane),
    path("get-name/<str:name>/", view_name),
    path("json/", json_view),
    path('index/', index),
    path('students/', students, name="students"),
    path('student/<int:id>/', student_detail, name="student_detail"),
    path('page1/', page1),
    path('', home)

]