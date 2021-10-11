from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import item


class itemForm(ModelForm):
    class Meta:
        model = item
        fields ='__all__'