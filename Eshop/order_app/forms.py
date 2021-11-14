from django import forms
from django.core import validators

from accounts_app.models import MyUser
from shop_app.models import Product


class OrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "cart-plus-minus-box"}),
        initial=1,
    )

    size = forms.CharField(
        widget=forms.HiddenInput(attrs={}),
    )

    color = forms.CharField(
        widget=forms.HiddenInput(attrs={}),
    )


class CheckOutForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "single-input"}),
        label="First Name: ",
        required=True,
        validators=[
            validators.MinLengthValidator(limit_value=3, message="first name length > 3")
        ]
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "single-input"}),
        label="Last Name: ",
        required=True,
        validators=[
            validators.MinLengthValidator(limit_value=3, message="last name length > 3")
        ]
    )
    city = forms.CharField(
        widget=forms.TextInput(),
        label="City: ",
        required=True,
    )
    address = forms.CharField(
        widget=forms.TextInput(),
        label="Address: ",
        required=True,
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "single-input"}),
        label="Phone Number: ",
        required=True,
        validators=[
            validators.MaxLengthValidator(limit_value=11, message="number length = 11"),
            validators.MinLengthValidator(limit_value=11, message="number length = 11")
        ]
    )
    post_code = forms.CharField(
        widget=forms.TextInput(attrs={"class": "single-input"}),
        label="Post Code: ",
        required=True,
        validators=[
            validators.MaxLengthValidator(limit_value=10, message="number length = 10"),
            validators.MinLengthValidator(limit_value=10, message="number length = 10")
        ]
    )
    text = forms.CharField(
        widget=forms.TextInput(),
        required=False
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
