from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from predict.models import *
from django.core.urlresolvers import reverse
import json
import pprint as pp

weight = {}
weight['TIME_SPENT'] = 0.4
weight['CLICKED'] = 0.2

# Create your views here.
def index(request):
    return HttpResponse("Index")

def input(request, id, list_id, action, param1=None, param2=None, param3=None):
    out = {}
    out_str = ""

    try:
        user = Profile.objects.get(id=id)
        listitem = ListItem.objects.get(id=list_id)
        ListItemAction.objects.create(profile=user, list_item=listitem, action=action, param1=param1, param2=param2, param3=param3)
        out['message'] = "Saved"

    except Exception as e:
        print str(e)
        out['error'] = str(e)

    out_str = json.dumps(out, indent=4)
    return HttpResponse(out_str)

def output(request, user):
    out = {}
    out['error'] = "None"
    out_str = ""
    try:
        user = Profile.objects.get(id=user)
        listitems = ListItem.objects.filter(profile=user)

        item_value = {}
        total_value = 0
        for i in listitems:
            listitemaction = ListItemAction.objects.filter(profile=user, list_item=i)
            value = 0
            for li in listitemaction:
                value += weight[li.action]*float(li.param1)

            item_value[i] = value
            total_value += value


        profile = {}
        profile['id'] = user.id
        profile['email'] = user.email
        out['profile'] = profile
        items = []
        time = 0.1
        for i in listitems:
            time += i.priority

        for i in listitems:
            item = {}
            item['content'] = i.content
            item['priority'] = item_value[i]/total_value
            items.append(item)
        out['items'] = items

    except Exception as e:
        print str(e)
        out['error'] = str(e)

    out_str = json.dumps(out, indent=4)

    return HttpResponse(out_str)


def populate(request):
    p, created = Profile.objects.get_or_create(email="pushkarkolhe@gmail.com", lastname="Kolhe", firstname="Pushkar")
    i = ListItem.objects.get_or_create(profile=p, content="content1", priority=0.0)
    ListItemAction.objects.get_or_create(profile=p, list_item=i[0], action="TIME_SPENT", param1="100")

    i = ListItem.objects.get_or_create(profile=p, content="content2", priority=0.0)
    ListItemAction.objects.get_or_create(profile=p, list_item=i[0], action="TIME_SPENT", param1="10")

    ListItem.objects.get_or_create(profile=p, content="content3", priority=0.0)
    ListItem.objects.get_or_create(profile=p, content="content4", priority=0.0)

    p, created = Profile.objects.get_or_create(email="shauvik@gmail.com", lastname="Roy", firstname="Shauvik")
    ListItem.objects.get_or_create(profile=p, content="content5", priority=0.0)
    i = ListItem.objects.get_or_create(profile=p, content="content5", priority=0.0)
    ListItemAction.objects.get_or_create(profile=p, list_item=i[0], action="TIME_SPENT", param1="200")

    i = ListItem.objects.get_or_create(profile=p, content="content6", priority=0.0)
    ListItemAction.objects.get_or_create(profile=p, list_item=i[0], action="TIME_SPENT", param1="50")


    ListItem.objects.get_or_create(profile=p, content="content6", priority=0.0)

    return HttpResponseRedirect(reverse('predict:index'))
