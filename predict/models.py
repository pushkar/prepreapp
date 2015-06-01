from django.db import models
from django.contrib import admin

# Create your models here.
class Profile(models.Model):
    email = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)

    def __unicode__(self):
            return str(self.firstname + " " + self.lastname)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email')
    search_fields = ('email', 'firstname', 'lastname')

class ListItem(models.Model):
    profile = models.ForeignKey(Profile)
    content = models.CharField(max_length=10000)
    priority = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return str(self.id)

class ListItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'content', 'priority')
    search_fields = ('priority',)

class ListItemAction(models.Model):
    created = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    list_item = models.ForeignKey(ListItem)
    action = models.CharField(max_length=50)
    param1 = models.CharField(max_length=20, null=True, blank=True)
    param2 = models.CharField(max_length=20, null=True, blank=True)
    param3 = models.CharField(max_length=20, null=True, blank=True)

class ListItemActionAdmin(admin.ModelAdmin):
    list_display = ('created', 'profile', 'list_item', 'action', 'param1', 'param2')
