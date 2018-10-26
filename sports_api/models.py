# -*- coding: utf-8 -*-
from django.db import models
from djongo import models
from django import forms

class Link(models.Model):
    """
    Link Model for storing Twitter Tweet related links url
    """
    link_url = models.CharField(max_length= 100)
    objects = models.DjongoManager()
    class Meta:
        abstract =True
    def __str__(self):
        return self.link_url
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields= ('link_url',)

class Tweet(models.Model):
    """
    Tweet Model for storing Twitter Tweet related details
    """
    text = models.CharField(max_length=200)
    id_str = models.CharField(max_length=200, primary_key=True)
    created_at = models.DateField()
    links = models.ArrayModelField(model_container=Link,model_form_class=LinkForm)
    objects = models.DjongoManager()

    def __str__(self):
        return self.text