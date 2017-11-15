# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
import urllib2
import re

# Create your views here.

def allrepos(request):
	try:
		package_list = []
		content_list = []
		count = 0
		repos_data = {	 
						'data' : [] ,
						'error status' : 0,
						'error msg' : ''
					}
		query_name = request.GET.get('q','')
		if query_name != '':
			url = 'https://api.github.com/search/repositories?q='+query_name+'&sort=stars&order=desc'
			response = urllib2.urlopen(url)
			my_data = json.loads(response.read().decode('utf-8'))
			items = my_data['items']
			for data in items:
				count = count + 1
				repos_data['data'].append(data)
				content_url = data['contents_url'][:-7]
				content_list.append(content_url)
				if count == 20:
					break

			for urls in content_list:
				print urls
				content_response = urllib2.urlopen(urls)
				content_data = json.loads(content_response.read().decode('utf-8'))
				for content in content_data:
					if content['name'] == 'requirements.txt' or content['name'] == 'requirements-dev.txt':
						requirement_url = content['download_url']
						print requirement_url
						requirement_response = urllib2.urlopen( requirement_url )
						for line in requirement_response:
							package = " ".join(re.findall("^[a-zA-Z]+[0-9]?", line))
							package_list.append(package)

			for pack in package_list:
				print pack
		else:
			raise Exception('no query parameter found in url.Please enter one')

	except Exception , e :
		repos_data['error status'] = 1
		repos_data['error msg'] = str (e)

	finally:
	
		json_data = json.dumps( repos_data , indent = 2)
		return HttpResponse( json_data , content_type = 'application/json')
