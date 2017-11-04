#!/usr/bin/env python
#encoding: utf-8
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import django,xlrd
from datetime import date
import json

sys.path.append('C:/Python27/Scripts/mysite') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 
django.setup()
from movie.models import Movie
s = list(Movie.objects.values_list('id', flat=1))
#img_url = Movie.objects.get(id=img)
	#print img_url.img.url




