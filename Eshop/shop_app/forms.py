from django import forms
from django.core import validators
from shop_app.models import ProductReview


class ProductReviewForm(forms.Form):
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"class": "review-input", "placeholder": "Enter Your E-mail"}),
        validators=[
            validators.EmailValidator()
        ]
    )

    text = forms.CharField(
        label="Share your opinion",
        widget=forms.Textarea(
            attrs={"class": "review-textarea", "id": "con_message", "name": "con_message",
                   "placeholder": "Enter Your message"})
    )

    product_ID = forms.IntegerField(
        widget=forms.HiddenInput()
    )
