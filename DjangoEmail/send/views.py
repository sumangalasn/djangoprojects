
# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import send


def testing(request):
    mydata = send.objects.all().values()
    template = loader.get_template('send/index.html')
    context = {
        'bysend': mydata,
    }
    return HttpResponse(template.render(context, request))