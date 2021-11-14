from django.core import validators

from django import forms


class BlogCommentsForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "coment-field", "placeholder": "Name"}),
        label="Name",
        validators=[
            validators.MaxLengthValidator(limit_value=200, message="Your name should not exceed 200 characters"),
            validators.MinLengthValidator(limit_value=3, message="Your name should not be less than 3 characters")
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "coment-field", "placeholder": "E-mail"}),
        label="E-mail",
        validators=[
            validators.EmailValidator()
        ]
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Write a comment"}),
        label="Text",
    )
    blog_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )
