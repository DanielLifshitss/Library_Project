from socket import create_server
from django.shortcuts import render, redirect
from .forms import NewUserForm, LoginForm
from .models import Customer, Book, Loan
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import timedelta,datetime


@login_required(login_url="register/")
def index(request):
    return render(request, "index.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                customer = Customer(name=cd["name"], city=cd["city"], age=cd["age"])
                customer.save()
                user = User.objects.create_user(
                    username=cd["name"], password=cd["password"]
                )
                user.save()
                login(request, user)
            except Exception as e:
                messages.error(request, "Username alredy exists.")
                return redirect(index)
            messages.success(request, "Registration successful.")
            return redirect(index)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "register.html", context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["name"], password=cd["password"])
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(
                    request, "Unsuccessful LOGIN. password or username dosnt exists."
                )
            return redirect("login")
    form = LoginForm()
    return render(request, "login.html", context={"form": form})


def logoutP(request):
    logout(request)
    return redirect("index")


def books_page(request):
    if request.method == "GET" and "bookname" in request.GET:
        title = request.GET["bookname"]
        author = request.GET["authorname"]
        if title is not None and title != "" and author is not None and author != "":
            books = Book.objects.filter(
                Q(name__contains=title) | Q(author__contains=author)
            )
        elif title is not None and title != "":
            books = Book.objects.filter(Q(name__contains=title))
        else:
            books = Book.objects.filter(Q(author__contains=author))
        return render(request, "books.html", {"books": books})
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


def add_or_remove_page(request):
    if request.method == "POST":
        add_book_title = request.POST.get("title")
        add_book_author = request.POST.get("author")
        add_book_year = request.POST.get("year")
        add_book_booktype = request.POST.get("booktype")
        remove_book_title = request.POST.get("title2")
        if (
            add_book_title is not None
            and add_book_title != ""
            and remove_book_title is None
            or remove_book_title == ""
        ):
            try:
                new_book = Book.objects.create(
                    name=add_book_title,
                    author=add_book_author,
                    year_published=add_book_year,
                    type=add_book_booktype,
                )
                new_book.save()
                messages.success(request, "Added book successfuly.")
            except:
                messages.error(request, "Unsuccessful Book Adding. Check the values.")
        elif remove_book_title is not None and remove_book_title != "":
            try:
                if (Book.objects.filter(name=remove_book_title)):
                    remove_book = Book.objects.filter(name=remove_book_title).delete()
                    messages.success(request, "Removing book successfuly.")
                    remove_book.save()
                else:
                    messages.error(request, "Unsuccessful Book Removing.")
            except:
                messages.error(request, "Unsuccessful Book Removing.")
    return render(request, "addremove.html")


def display_loan_page(request):
    loans = Loan.objects.all().values(
        "customer__name", "book__name", "loandate", "returndate"
    )
    print(loans)
    return render(request, "loans.html", {"loans": loans})


def loan_or_return_page(request):
    if request.method == "POST":
        loan_book = request.POST.get("title")
        return_book = request.POST.get("title2")
        if loan_book is not None and loan_book != '' and Loan.objects.values("book__name") != loan_book:
            print("------------")
            my_date_str = datetime.now()
            formatted_datetime = my_date_str.strftime(r"%y/%m/%d %H:%M:%S")
            format_str = str(r"%y/%m/%d %H:%M:%S")
            my_date = datetime.strptime(str(formatted_datetime), format_str)
            if Book.objects.filter(name=loan_book) and Book.objects.filter(type=int(1)):
                days_to_add = 10
                delta = timedelta(days=days_to_add)
                new_date = my_date + delta
                username = request.user.get_username()
                print(username)
                if Customer.objects.filter(name=username):
                    customer = Customer.objects.filter(name=username).values('id')
                    book = Book.objects.filter(name=loan_book).values('id')
                    add_load_book = Loan.objects.create(customer=customer,Book=book,loandate=my_date_str,returndate=new_date)
                    add_load_book.save()
                    messages.success(request, "Book Loanded.")
                    print("ok")
                else:
                    print("not ok")
            elif Book.objects.filter(name=loan_book) and Book.objects.filter(type=int(2)):
                days_to_add = 5
                delta = timedelta(days=days_to_add)
                new_date = my_date + delta
                username = request.user.get_username()
                print(username)
                if Customer.objects.filter(name=username):
                    customer = Customer.objects.filter(name=username).values('id')
                    book= Book.objects.filter(name=loan_book).values('id')
                    print(customer)
                    print(book)
                    print("--------------")
                    add_load_book = Loan(castomer=customer[0]['id'],book=book[0]['id'],loandate=my_date_str,returndate=new_date)
                    add_load_book.save()
                    messages.success(request, "Book Loanded.")
                    print("ok")
                else:
                    print("not ok")
            elif Book.objects.filter(name=loan_book) and Book.objects.filter(type=int(3)):
                days_to_add = 2
                delta = timedelta(days=days_to_add)
                new_date = my_date + delta
                username = request.user.get_username()
                print(username)
                if Customer.objects.filter(name=username):
                    customer = Customer.objects.filter(name=username).values('id')
                    book= Book.objects.filter(name=loan_book).values('id')
                    print(customer)
                    print(book)
                    print("--------------")
                    add_load_book = Loan(castomer=customer[0]['id'],book=book[0]['id'],loandate=my_date_str,returndate=new_date)
                    add_load_book.save()
                    messages.success(request, "Book Loanded.")
                    print("ok")
                else:
                    print("not ok")
            else:   
                messages.error(request, "Unsuccessful Book Removing.")
    return render(request, "loanandreturn.html")


def personalP(request):
    username = request.user.get_username()
    customer = Customer.objects.filter(name=username).values('id')
    loans = Loan.objects.filter(customer=customer[0]['id'])
    return render(request, "personal.html",  {"loans": loans})