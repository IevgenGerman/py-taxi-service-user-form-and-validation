from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from taxi.models import Driver


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "license_number")

