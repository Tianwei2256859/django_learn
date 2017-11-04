# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import Movie, Movie_info
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def movie_list(request, template = 'movie/base.html'):
	if request.method =='GET':
		param = request.GET.get('param', '')
    	movies = Movie.objects.filter(title__icontains = param)
    	return render(request, template, {"movies": movies})

def movie_detail(request, data, template = 'movie/detail.html' ):
	movie_detail = list(Movie.objects.filter(id = data).values('title', 'director', 'screenwriter',
			'actors', 'types', 'regions', 'initialreleasedate', 'runtime', 'related_info',
			'score'))
	info = Movie_info.objects.get(id = data)
	obj = Movie.objects.get(id = data)
	img_url = obj.img.url
	title_info = info.title_info
	release_date = info.release_date
	return  render(request, template, {'movie_detail': movie_detail, 'title_info':title_info, 
		'release_date': release_date,'img_url': img_url})

def index(request, template = 'movie/base.html'):
	types = request.GET.get('tags')
	
	movies = Movie.objects.filter(types__icontains = types)
	return render(request, template, {"movies": movies, "types": types})

	





