from django import forms

from django.core import validators


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-group", "placeholder": "Enter your name"}),
        label="Your Name",
        validators=[
            validators.MaxLengthValidator(limit_value=200, message="max limit 200 characters"),
            validators.MinLengthValidator(limit_value=3, message="min limit 3 characters")
        ]

    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-group", "placeholder": "Enter your email"}),
        label="Your Email",
        validators=[
            validators.EmailValidator()
        ]

    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-group", "placeholder": "Enter your subject"}),
        label="Subject",
        validators=[
            validators.MaxLengthValidator(limit_value=100, message="max limit 100 characters"),
            validators.MinLengthValidator(limit_value=3, message="min limit 3 characters")
        ]

    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-group form-group-2", "placeholder": "Enter your name"}),
        label="Your Message",

    )
