from django.db import models
from django.contrib import admin

class ReferencedActSection(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    act_name = models.CharField(max_length=100, unique=True) # TODO: could we use a URL to identify the act?
    section = models.IntegerField()

    def __str__(self):
        return f'{self.act_name} - §{self.section}'


class Offence(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    offence_name = models.CharField(max_length=100, unique=True)
    referenced_acts = models.ManyToManyField(ReferencedActSection, blank=True)
    effective_from = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.offence_name

admin.site.register(Offence)
admin.site.register(ReferencedActSection)