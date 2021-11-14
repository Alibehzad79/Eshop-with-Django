from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

from accounts_app.models import MyUser
from django.contrib.auth.forms import AuthenticationForm


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = "__all__"

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    remember = forms.BooleanField(

    )


class EditProfile(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "single-input"}),
        label="First Name: ",
        required=False,
        validators=[
            validators.MinLengthValidator(limit_value=3, message="first name length > 3")
        ]
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "single-input"}),
        label="Last Name: ",
        required=False,
        validators=[
            validators.MinLengthValidator(limit_value=3, message="last name length > 3")
        ]
    )
    city = forms.CharField(
        widget=forms.TextInput(),
        label="City: ",
        required=False,
    )
    address = forms.CharField(
        widget=forms.TextInput(),
        label="Address: ",
        required=False,
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': "10", "cols": "40"}),
        label="Description: ",
        required=False
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "single-input"}),
        label="Phone Number: ",
        required=False,
        validators=[
            validators.MaxLengthValidator(limit_value=11, message="number length = 11"),
            validators.MinLengthValidator(limit_value=11, message="number length = 11")
        ]
    )
    post_code = forms.CharField(
        widget=forms.TextInput(attrs={"class": "single-input"}),
        label="Post Code: ",
        required=False,
        validators=[
            validators.MaxLengthValidator(limit_value=10, message="number length = 10"),
            validators.MinLengthValidator(limit_value=10, message="number length = 10")
        ]
    )

    profile_image = forms.ImageField(

    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        try:
            phone_number = int(phone_number)
        except:
            raise forms.ValidationError(message="no string")
        return phone_number

    def clean_post_code(self):
        post_code = self.cleaned_data.get("post_code")
        try:
            post_code = int(post_code)
        except:
            raise forms.ValidationError(message="no string")
        return post_code
