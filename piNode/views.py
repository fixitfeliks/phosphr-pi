import os
import sys
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEW_DIR = os.path.join( BASE_DIR, 'html/index.html')
sys.path.append(os.path.join( BASE_DIR,'lib'))
import pi_light

from django.shortcuts import render
from gpiozero import RGBLED, LED, PWMLED, RGBLED
from django.template.response import TemplateResponse
from django.http import HttpResponse


print(NEW_DIR)
#led = RGBLED(red=27,green=17,blue=22)

def index(request, template_name=NEW_DIR):
    #future code read file see if user is registered
    #expirey?

    registered = False
    if registered:
        pass
    else:
        args = {}
        text = pi_light.getId()
        args['id'] = text
        return TemplateResponse(request, template_name, args)



def test(request):
    red = request.GET.get('r',0)
    green = request.GET.get('g',0)
    blue = request.GET.get('b',0)
    print ("reqVar: ")

    led.color = (float(red),float(green),float(blue))
    return HttpResponse("brightness set to " + red + " , " + green + " , " + blue)
