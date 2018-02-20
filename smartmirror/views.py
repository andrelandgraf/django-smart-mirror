from django.http import HttpResponse, Http404
from django.utils import timezone
from django.template import loader

import fnmatch, os, base64
from djangosmartmirror import settings

def index(request):
    datetime = str(timezone.now().date())+" "+str(timezone.now().time())
    imgcount = len(fnmatch.filter(os.listdir(settings.BASE_DIR+'/smartmirror/static/smartmirror/img/'), '*.jpg'))

    template = loader.get_template('smartmirror/index.html')
    context = {
        "datetime": datetime,
        "imgcount": imgcount,
    }

    return HttpResponse(template.render(context, request))

def showimage(request, imgid):
    img_nr = imgid
    try:
        with open(settings.BASE_DIR+'/smartmirror/static/smartmirror/img/img'+str(img_nr)+'.jpg', "rb") as f:
            return HttpResponse(base64.b64encode(f.read()), content_type="image/jpeg")
    except IOError:
        raise Http404("Image does not exist")
