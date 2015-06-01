from django.contrib import admin
from predict.models import *

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(ListItem, ListItemAdmin)
admin.site.register(ListItemAction, ListItemActionAdmin)
