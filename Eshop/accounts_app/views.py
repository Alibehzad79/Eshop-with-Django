from django.contrib.auth.views import auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from accounts_app.forms import SignupForm, LoginForm
from accounts_app.forms import EditProfile

# Create your views here.
from accounts_app.models import MyUser


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "accounts/registration/register.html"
    form_class = SignupForm
    success_message = "Your profile was created successfully"
    success_url = "/accounts/login/"


@login_required(login_url='/accounts/login/')
def dashboard(request, **kwargs):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, 'accounts/registration/dashboard.html', context)


@login_required(login_url='/accounts/login/')
def edit_account_details(request, **kwargs):
    user = MyUser.objects.get(id=request.user.id)
    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES,
                           initial={'post_code': user.post_code, 'phone_number': user.phone_number}, )
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            address = form.cleaned_data.get("address")
            phone_number = form.cleaned_data.get("phone_number")
            post_code = form.cleaned_data.get("post_code")
            description = form.cleaned_data.get("description")
            profile_image = form.cleaned_data.get("profile_image")
            phone_number = int(phone_number)
            post_code = int(post_code)

            user.first_name = first_name
            user.last_name = last_name
            user.address = address
            user.description = description
            user.post_code = post_code
            user.phone_number = phone_number
            user.profile_image = profile_image
            user.save()
            return redirect("edit-account-detail")

    else:
        form = EditProfile()

    context = {
        "form": form,
        "user": user,

    }
    return render(request, 'accounts/registration/edit_account_details.html', context)
