from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, TeacherForm, StudentForm, StudentProfileForm, CourseForm, ClassForm
from django.shortcuts import get_object_or_404
from .models import User
from courses.models import Course, ClassRoom


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login_view")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password"})
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login_view")


@login_required
def dashboard(request):
    role = request.user.role
    if role == "admin":
        return render(request, "accounts/admin_dashboard.html")
    elif role == "principal":
        return render(request, "accounts/principal_dashboard.html")
    elif role == "teacher":
        return render(request, "accounts/teacher_dashboard.html")
    elif role == "student":
        return render(request, "accounts/student_dashboard.html")
    elif role == "parent":
        return render(request, "accounts/parent_dashboard.html")
    else:
        return redirect("login_view")


@login_required
def teacher_list(request):
    if request.user.role != "principal":
        return redirect("dashboard")
    teachers = User.objects.filter(role="teacher")
    return render(request, "accounts/teacher_list.html", {"teachers": teachers})

@login_required
def teacher_create(request):
    if request.user.role != "principal":
        return redirect("dashboard")
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    else:
        form = TeacherForm()
    return render(request, "accounts/teacher_form.html", {"form": form})

@login_required
def teacher_edit(request, pk):
    if request.user.role != "principal":
        return redirect("dashboard")
    teacher = get_object_or_404(User, pk=pk, role="teacher")
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "accounts/teacher_form.html", {"form": form})

@login_required
def teacher_delete(request, pk):
    if request.user.role != "principal":
        return redirect("dashboard")
    teacher = get_object_or_404(User, pk=pk, role="teacher")
    teacher.delete()
    return redirect("teacher_list")

# Create your views here.
def manage_courses(request):
    courses = Course.objects.all()
    return render(request, "accounts/manage_courses.html", {"courses": courses})

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_courses")
    else:
        form = CourseForm()
    return render(request, "accounts/add_course.html", {"form": form})

# ✅ Manage Classes
def manage_classes(request):
    classes = ClassRoom.objects.all()
    return render(request, "accounts/manage_classes.html", {"classes": classes})

def add_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_classes")
    else:
        form = ClassForm()
    return render(request, "accounts/add_class.html", {"form": form})

def manage_students(request):
    students = User.objects.filter(role="student")
    return render(request, "accounts/manage_students.html", {"students": students})

def add_student(request):
    if request.method == "POST":
        user_form = StudentForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            student = user_form.save(commit=False)
            student.set_password(user_form.cleaned_data['password'])
            student.role = "student"
            student.save()
            profile = profile_form.save(commit=False)
            profile.student = student
            profile.save()
            return redirect("manage_students")
    else:
        user_form = StudentForm()
        profile_form = StudentProfileForm()
    return render(request, "accounts/add_student.html", {"user_form": user_form, "profile_form": profile_form})