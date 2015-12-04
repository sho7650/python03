import SoftLayer
from django.shortcuts import render
from accounts.models import CustomUser
from accounts.models import softlayer_api

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def user_list(request):
    users = softlayer_api.objects.all().order_by('id')
    return render_to_response('user_list.html', {'users': users}, context_instance=RequestContext(request))

def account_list(request):
    loginname = None
    if request.user.is_authenticated():
        loginname = request.user.username
    username = CustomUser.objects.get(username=loginname)
#    pk     = username.softlayer_id
    user   = softlayer_api.objects.get(pk=username.softlayer_id)
    client = SoftLayer.create_client_from_env(username=user.username, api_key=user.api_key)
    acct   = client['Account'].getUsers()
#    return HttpResponse(acct)
    return render_to_response('account_list.html', {'accounts': acct}, context_instance=RequestContext(request))
