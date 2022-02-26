from pickle import FALSE
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VendorDetails
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Parent, Child
import uuid
from django.contrib.auth import login, authenticate  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this


# Create your views here.

def Index(request):
    signedIn = True
    parentFlag = True
    args = {"signedIn": signedIn, "parentFlag": parentFlag}
    return render(request, 'app/homepage.html', args)


def SignIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="app/sign-in.html", context={"login_form": form})


def SignUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            parent = Parent()
            parent.first_name = request.POST.get("first_name")
            parent.last_name = request.POST.get("last_name")
            parent.user_name = request.POST.get("username")
            parent.email_id = request.POST.get("email")
            parent.password = request.POST.get("password1")
            parent.random_id = uuid.uuid4()

            parent.save()

            print('This is the parent first name: ' + parent.first_name)

            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return render(request=request, template_name="app/sign-in.html")

        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="app/sign-up.html", context={"register_form": form})


@csrf_exempt
def ChildDashboard(request):
    render_string = render_to_string("app/child-dashboard.html")

    return HttpResponse(render_string)


@csrf_exempt
def ChildMarketPlace(request):
    vendors = VendorDetails.objects.all()
    args = {"vendors": vendors}
    render_string = render_to_string("app/market-place.html", args)

    return HttpResponse(render_string)


@csrf_exempt
def ChildCourses(request):
    render_string = render_to_string("app/courses.html")

    return HttpResponse(render_string)

@csrf_exempt
def ParentDashboard(request):
    render_string = render_to_string("app/parent-dashboard.html")

    return HttpResponse(render_string)
