from django.shortcuts import render
from django.template import Context, loader, RequestContext
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import csv
from modiusers.models import LogEntry, CustomUser
from django.http import HttpResponse
import pdb
from django.conf import settings

def index(request):
    allofit = []
    for logs in LogEntry.objects.all()[:10]:
        cus = CustomUser.objects.filter(doorkey=logs.doorkey)
        if cus.exists():
            allofit.append({'doorkey':'sandwich','name':'5200','date':'date','image':'imageurl','validentry':'True'})
        else:
            allofit.append({'doorkey':'sandwich','name':'5200','date':'date','image':'imageurl','validentry':'True'})
    return render(request, 'index.html', allofit)

   

@csrf_exempt
def door_login(request):
    state = "LOGIN"
    key = ''

    
    ip = request.META['REMOTE_ADDR']
    if request.POST:

        doorkey = request.POST.get('doorkey')
        extra = request.POST.get('extra')
        
        user = authenticate(doorkey=doorkey, extra=extra)
        
        if ip in settings.INTERNAL_IPS:
            if user is not None:
                if user.is_active:
                    login(request, user)
                    state = "LOGEDIN"
                else:
                    state = "NOTACTIVE"
            else:
                state = "INCORRECT"
        else:
            state = "NOTFROMTHERE"
    else:
        state = "GOTAGIVEKEY"

    response = HttpResponse(content_type='text/plain')
    # response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['MSG', state,'IP',ip])

    return response


def login_user(request):
    state = "Please log in below..."
    doorkey = ''
    c = {}
    # c.update(csrf(request))

    if request.POST:

        doorkey = request.POST.get('doorkey')
        user = authenticate(doorkey=doorkey)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your doorkey was incorrect."

    c.update({'state':state, 'doorkey': doorkey})
    return render_to_response('auth.html',c)# Create your views here.
