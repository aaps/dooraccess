from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
import pdb

def login_user(request):
    state = "Please log in below..."
    doorkey = ''
    c = {}
    c.update(csrf(request))

    if request.POST:

        doorkey = request.POST.get('doorkey')
        # user = User.objects.get(doorkey=doorkey)
        # pdb.set_trace()
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
