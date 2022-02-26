from pickle import FALSE
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .models import User
import uuid
from django.contrib.auth import login, authenticate  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this


# Create your views here.

def Index(request):
    signedIn = False
    parentFlag = False
    args = {"signedIn": signedIn, "parentFlag": parentFlag}
    return render(request, 'app/homepage.html', args)


@csrf_exempt
def SignIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            parentFlag = request.POST.get('is-parent')

            print(form.cleaned_data)

            print(type(parentFlag))

            print("Parent flag is: " + str(parentFlag))

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")

                print(type(user))

                temp = User.objects.filter(user_name=user)
                if temp[0].user_type == 0:
                    parentFlag = False
                else:
                    parentFlag = True
                signedIn = True

                args = {"signedIn": signedIn, "parentFlag": parentFlag}
                return render(request, 'app/homepage.html', args)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="app/sign-in.html", context={"login_form": form})


@csrf_exempt
def SignUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = User()
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.user_name = request.POST.get("username")
            user.email_id = request.POST.get("email")
            user.password = request.POST.get("password1")
            user.random_id = uuid.uuid4()

            if request.POST.get("is-parent") == "no":
                user.user_type = 0
            else:
                user.user_type = 1

            user.save()
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
