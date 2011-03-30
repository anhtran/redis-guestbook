from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from notebook import redoc


def index(request):
    items = redoc.getRedis(number=30)
    return render_to_response('guestbook/index.html',
                              { 'items': items, }, context_instance=RequestContext(request))


@csrf_protect
def ajax_save(request):
    msgr = ""
    if request.is_ajax():
        username = request.POST.get('username', False)
        message = request.POST.get('message', False)
        if username and message:
            data = []
            data.append(username)
            data.append(message)
            try:
                redoc.saveRedis(data)
            except:
                msgr = "Cannot save data to redis."
        else:
            msgr = "Something was missing!"
    else:
        msgr = "No no, this is not the name of a football club!!!"
    return HttpResponse(msgr)