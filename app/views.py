from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from .forms import NewUserForm
from django.contrib.auth import login
# from .forms import CustomerRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# # from . models import Product
from django.contrib import messages

# from waste_management.app.models import Product

# Create your views here.

def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

class CategoryView(View):
    def get(self, request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html",locals())
    
class CategoryTitle(View):
    def get(self, request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html",locals())
    
class ProductDetail(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/productdetail.html",locals())
    
# class CustomerRegistrationView(View):
#     def get(self, request):
#         form = CustomerRegistrationForm()
#         return render(request, "app/customerregistration.html",locals())
#     def post(self, request):
#         form = CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Congratulations! User Register Successfully")
#         else:
#             messages.error(request, "Invalid Input Data")
#         return render(request, "app/customerregistration.html",locals())

# class CustomerRegistrationView(View):
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("app:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="app\customerregistration.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("app:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="app\login.html", context={"login_form":form})
