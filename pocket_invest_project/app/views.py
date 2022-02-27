from inspect import ArgSpec
from pickle import FALSE
import re
from this import d
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .models import CaseStudies, Investment, Relationship, User
from .models import Transaction, User, Course, Module, ModuleProg, Question
import uuid
from datetime import datetime
from django.contrib.auth import login, authenticate  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this
import json
from django.core.mail import EmailMessage


# Create your views here.
@csrf_exempt
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

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                temp = User.objects.filter(user_name=user)

                if temp[0].user_type == 0:
                    parentFlag = False
                else:
                    parentFlag = True
                signedIn = True
                args = {"signedIn": signedIn,
                        "parentFlag": parentFlag, "user": temp[0]}
                return render(request, 'app/homepage.html', args)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    print("I'm here")
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
            random_id = uuid.uuid4()
            user.random_id = random_id

            if request.POST.get("is-parent") == "no":
                user.user_type = 0
            else:
                user.user_type = 1
                email = EmailMessage('Thanks for signing-up on Pocket Invest!', 'Here is your unique key which you can use to connect to your children on Pocket Invest - ' + str(random_id), to=[request.POST.get("email")])
                email.send()

            if(user.user_type == 0):
                user.real_money_balance = 0
                user.virtual_money_balance = 0
                user.gender = 0

            user.gender = request.POST.get("gender")
            user.age = request.POST.get("age")

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
    username = request.POST.get('username')
    print(username)
    child = User.objects.filter(user_name=username)
    print(child)
    args = {"child": child[0]}
    render_string = render_to_string("app/child-dashboard.html", args)

    return HttpResponse(render_string)


@csrf_exempt
def ChildMarketPlace(request):
    username = request.POST.get("username")
    user = User.objects.filter(user_name=username)
    vendors = User.objects.filter(user_type=2)
    args = {"vendors": vendors, "user": user[0]}
    render_string = render_to_string("app/market-place.html", args)

    return HttpResponse(render_string)


@csrf_exempt
def ChildCourses(request):
    username = request.POST.get("username")
    user = User.objects.filter(user_name=username)
    courses = Course.objects.all()
    args = {"courses": courses, "user": user[0]}
    render_string = render_to_string("app/courses.html", args)

    return HttpResponse(render_string)


@csrf_exempt
def ParentDashboard(request):
    username = request.POST.get("username")
    user = User.objects.filter(user_name=username)

    # chart 1 get parent transactions
    transactions = Transaction.objects.all().order_by('-date')
    transaction_ids = Transaction.objects.filter(
        sender=user[0], type_of_transaction=0).order_by('receiver').order_by('date')

    listOfDict = []
    mapOfChart1 = {}
    for x in transaction_ids:
        # print("printing name " + x.receiver.first_name)
        print("printing date " + str(x.date).split('-')[1])
        month = int(str(x.date).split('-')[1])
        if x.receiver.first_name in mapOfChart1:
            data = mapOfChart1[x.receiver.first_name]
            data[month - 1] += int(x.amount)
        else:
            data = [0] * 12
            mapOfChart1[x.receiver.first_name] = data
            data[month - 1] = int(x.amount)

    for key in mapOfChart1:
        tempDict = {}
        tempDict["name"] = key
        tempDict["data"] = mapOfChart1[key]
        listOfDict.append(tempDict)

    # chart 2 - get child money status
    realMoney = 0
    virtualMoney = 0
    relationships = Relationship.objects.filter(parent=user[0])
    for x in relationships:
        realMoney += x.child.real_money_balance
        virtualMoney += x.child.virtual_money_balance

    print(virtualMoney)
    print(realMoney)
    virtualRealPieChartArgs = [
        ['Real Money', realMoney], ['Virtual Money', virtualMoney]]

    # chart 4 - get child expenditures
    listOfDict4 = []
    for y in relationships:
        print("Y - ")
        print(y.child.first_name)
        transaction_ids = Transaction.objects.filter(
            sender=y.child, type_of_transaction=1).order_by('receiver').order_by('date')

        mapOfChart4 = {}
        for x in transaction_ids:
            # print("printing name " + x.receiver.first_name)
            print("printing date " + str(x.date).split('-')[1])
            month = int(str(x.date).split('-')[1])
            if x.sender.first_name in mapOfChart4:
                data4 = mapOfChart4[x.sender.first_name]
                data4[month - 1] += int(x.amount)
            else:
                data4 = [0] * 12
                mapOfChart4[x.sender.first_name] = data4
                data4[month - 1] = int(x.amount)

        tempDict4 = {}
        tempDict4["name"] = y.child.first_name
        tempDict4["data"] = mapOfChart4[y.child.first_name]
        listOfDict4.append(tempDict4)

    args = {"user": user[0], "transactions": transactions,
            "chart1": json.dumps(listOfDict), "chart2": json.dumps(virtualRealPieChartArgs), "chart4": json.dumps(listOfDict4)}
    render_string = render_to_string("app/parent-dashboard.html", args)

    return HttpResponse(render_string)


@csrf_exempt
def ParentAddMoney(request):
    username = request.POST.get("username")
    print("My username ", username)
    user = User.objects.filter(user_name=username)
    print('inside parent add money function')
    print(user)
    relationships = Relationship.objects.filter(parent=user[0])
    args = {"relationships" : relationships, "user" : user[0]}
    render_string = render_to_string("app/parent-add-money.html", args)

    return HttpResponse(render_string)

@csrf_exempt
def ParentUpdateMoney(request):
        inputAmount = request.POST.get("amountToAdd")
        childSelect = request.POST.get("child")
        operation = request.POST.get("operation")
        
        child = User.objects.filter(first_name=childSelect)
        if(operation == 'add'):
            child.update(real_money_balance=(int(child[0].real_money_balance) + int(inputAmount)))
            if(child[0].gender == 1):
                child.update(virtual_money_balance=(int(child[0].virtual_money_balance) + int(int(inputAmount)*1.5)))
            else:
                child.update(virtual_money_balance=(int(child[0].virtual_money_balance) + int(inputAmount)))
        elif(operation == 'subtract' and int(child[0].real_money_balance) - int(inputAmount) > 0):
            child.update(real_money_balance=(int(child[0].real_money_balance) - int(inputAmount)))
        
        render_string = render_to_string("app/parent-dashboard.html")

        return HttpResponse(render_string)

@csrf_exempt
def Profile(request):
    if request.POST and "submit-access-code" not in request.POST:
        currentusername = request.POST.get("user")
        print(currentusername)
        args = {"currentusername": currentusername}
        return render(request, 'app/profile.html', args)

    if request.POST and "submit-access-code" in request.POST:
        uniqueStringToSearch = request.POST.get("access_code")

        # get current and parent user strings
        currentusername = request.POST.get("hiddencurrentuser")
        parentusername = request.POST.get("username")

        print(currentusername)
        print(parentusername)

        # fetch current and parent user objects
        currentUserObject = User.objects.filter(user_name=currentusername)
        parentUserObject = User.objects.filter(user_name=parentusername)

        print(currentUserObject)
        print(parentUserObject)

        # add data to relationship model
        relationship = Relationship()
        relationship.parent = parentUserObject[0]
        relationship.child = currentUserObject[0]
        relationship.random_id = uniqueStringToSearch

        if uniqueStringToSearch == parentUserObject[0].random_id:
            relationship.save()
            signedIn = True
            parentFlag = False
            args = {"signedIn": signedIn, "parentFlag": parentFlag}
            return render(request, 'app/homepage.html', args)
        else:
            print('Random ID did not match')
            signedIn = True
            parentFlag = False
            args = {"signedIn": signedIn, "parentFlag": parentFlag}
            return render(request, 'app/homepage.html', args)
        return render(request, 'app/profile.html')


@csrf_exempt
def BuyItem(request):

    cost = request.POST['value']
    name = request.POST['name']
    child_username = request.POST['user_name']
    title = ''
    body = ''
    child = User.objects.filter(user_name=child_username)

    if int(child[0].virtual_money_balance) >= int(cost):
        child[0].virtual_money_balance = int(
            child[0].virtual_money_balance)-int(cost)
        child.update(virtual_money_balance=(
            int(child[0].virtual_money_balance)-int(cost)))
 # To Implement: Email to parent
        body = 'Congratulations! You just purchased a gift card from ' + \
            name + ' worth ' + cost + ' points.'
        title = 'Transaction Successful!'
        transaction = Transaction()
        transaction.sender = child[0]
        transaction.receiver = child[0]  # To update
        transaction.amount = cost
        transaction.date = datetime.today()
        transaction.details = 'purchased a gift card from ' + \
            name + ' worth ' + cost + ' points.'
        transaction.outcome = "Successful"
        transaction.type_of_transaction = 1  # To be updated
        transaction.save()

    else:
        body = 'Oops! You do not have sufficient balance to buy this item. You can invest your money to earn more points to buy more exciting stuff!'
        title = 'Insufficient balance'

    print(title)
    response = {'title': title, 'message': body}
    return JsonResponse(response)


@csrf_exempt
def Quiz(request):

    username = request.POST.get("username")
    coursename = request.POST.get("coursename")
    count = request.POST.get("count")
    user = User.objects.filter(user_name=username)
    course = Course.objects.filter(course_name=coursename)
    # progress=ModuleProgress()
    question_count=0
    questions=Question.objects.filter(course_id=course[0].id)
    
    obj = ModuleProg.objects.filter(course_id=course[0].id, user_id=user[0].id)
    if(obj.count()==0):
        obj = ModuleProg(course_id=course[0].id, user_id=user[0].id, module_count=count)
        obj.save()
    else:
        obj.update(module_count=(int(obj[0].module_count)+int(count)))

    print(questions[question_count].option_1)

    args = {"user":user[0], "coursename":coursename, "questions":questions[question_count],"count":question_count}


    render_string = render_to_string("app/quiz.html",args)

    return HttpResponse(render_string)


@csrf_exempt
def Quiz2(request):

    username = request.POST.get("username")
    coursename = request.POST.get("coursename")
    count = request.POST.get("count")
    user = User.objects.filter(user_name=username)
    course = Course.objects.filter(course_name=coursename)
    # progress=ModuleProgress()
    question_count=int(count)+1

    if(question_count>2):
            modules = Module.objects.filter(course_id=course[0].id)
            args = {"modules": modules,"user":user[0], "coursename":coursename}
            render_string = render_to_string("app/module.html",args)
            return HttpResponse(render_string)

    questions=Question.objects.filter(course_id=course[0].id)
    args = {"user":user[0], "coursename":coursename, "questions":questions[question_count],"count":question_count}


    render_string = render_to_string("app/quiz.html",args)

    return HttpResponse(render_string)


@csrf_exempt
def module(request):
    username = request.POST.get("username")
    topic = request.POST.get("topic")
    coursename = request.POST.get("coursename")
    user = User.objects.filter(user_name=username)
    course = Course.objects.filter(course_name=coursename)
    modules = Module.objects.filter(course_id=course[0].id)
    args = {"modules": modules,"user":user[0], "topic":topic, "coursename":coursename}

@csrf_exempt
def Portfolio(request):
    username = request.POST.get('username')
    user = User.objects.filter(user_name=username)
    total_investment_value = 0
    current_investment_value = 0
    percentage_change = 0
    investments = Investment.objects.filter(child=user[0])
    for x in investments:
        total_investment_value += x.amount_invested
        current_investment_value += x.current_investment_value

    if (total_investment_value == 0 or current_investment_value == 0):
        total_investment_value = 0
        current_investment_value = 0
        percentage_change = 0
    else:
        percentage_change = round(
            ((current_investment_value - total_investment_value) / total_investment_value) * 100, 2)

    if request.method == "POST" and 'investmentid' in request.POST:
        # 1. change overall view of investment
        # 2. chnage money value in wallet
        # 3. delete from investments
        investmentid = request.POST.get('investmentid')
        investment = Investment.objects.filter(id=investmentid)
        total_investment_value -= investment[0].amount_invested
        current_investment_value -= investment[0].current_investment_value

        if (total_investment_value == 0 or current_investment_value == 0):
            total_investment_value = 0
            current_investment_value = 0
            percentage_change = 0
        else:
            percentage_change = round(
                ((current_investment_value - total_investment_value) / total_investment_value) * 100, 2)

        # user[0].virtual_money_balance = int(user[0].virtual_money_balance) + int(investment[0].current_investment_value)
        user.update(virtual_money_balance=(
            int(user[0].virtual_money_balance) + int(investment[0].current_investment_value)))

        Investment.objects.filter(id=investmentid).delete()
        investments = Investment.objects.filter(child=user[0])

        args = {"username": username, "investments": investments, "total_investment_value": total_investment_value,
                "current_investment_value": current_investment_value, "percentage_change": percentage_change}
        print(investments)
        render_string = render_to_string("app/portfolio.html", args)
        return HttpResponse(render_string)

    if request.method == 'POST' and 'purpose' in request.POST:
        # 1. Delete money from wallet
        # 2. Add investment row in investment table
        case_study_id = request.POST.get("case_study")
        case_study = CaseStudies.objects.filter(id=case_study_id)
        investmentBuy = Investment()
        investmentBuy.child = user[0]
        investmentBuy.investment_name = case_study[0].case_study_investment_name
        investmentBuy.amount_invested = case_study[0].case_study_value
        investmentBuy.current_investment_value = case_study[0].case_study_value
        investmentBuy.save()
        investments = Investment.objects.filter(child=user[0])

        user.update(virtual_money_balance=(
            int(user[0].virtual_money_balance) - int(case_study[0].case_study_value)))
    case_studies = CaseStudies.objects.all()

    args = {"username": username, "investments": investments, "total_investment_value": total_investment_value,
            "current_investment_value": current_investment_value, "percentage_change": percentage_change, "case_studies": case_studies}
    print(investments)

    render_string = render_to_string("app/portfolio.html", args)

    return HttpResponse(render_string)
