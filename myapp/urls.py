from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("todos/",views.todos,name="todos"),
    path("tests/",views.tests,name="tests"),
    path("about/",views.about,name="about")
]