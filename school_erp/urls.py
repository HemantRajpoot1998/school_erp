"""
URL configuration for school_erp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import (
    register_view,
    login_view,
    logout_view,
    dashboard,
    teacher_list,
    teacher_create,
    teacher_edit,
    teacher_delete,
    manage_courses,
    add_course,
    manage_classes,
    add_class,
    manage_students,
    add_student,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register_view, name="register_view"),
    path("", login_view, name="login_view"),
    path("logout/", logout_view, name="logout_view"),
    path("dashboard/", dashboard, name="dashboard"),

    # Teacher management (Principal only)
    path("teachers/", teacher_list, name="teacher_list"),
    path("teachers/create/", teacher_create, name="teacher_create"),
    path("teachers/<int:pk>/edit/", teacher_edit, name="teacher_edit"),
    path("teachers/<int:pk>/delete/", teacher_delete, name="teacher_delete"),

    path("courses/", manage_courses, name="manage_courses"),
    path("courses/add/", add_course, name="add_course"),

    path("classes/", manage_classes, name="manage_classes"),
    path("classes/add/", add_class, name="add_class"),

    path("students/", manage_students, name="manage_students"),
    path("students/add/", add_student, name="add_student"),
]
