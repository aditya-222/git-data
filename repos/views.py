# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
import urllib2
import re
from collections import Counter

def allrepos(request):
	try:
		package_list = []
		packages = {
						'name' : '',
						'count': 0,
		}
		count = 0
		header = ('User-Agent' , 'aditya-22')
		repos_data = {	 
						'data' : [] ,
						'package_count' :[] ,
						'error status' : 0,
						'error msg' : ''
					}
		query_name = request.GET.get('q','')
		if query_name != '':
			url = 'https://api.github.com/search/repositories?q='+query_name+'&sort=stars&order=desc'	
			repo_request = urllib2.Request( url )
			repo_request.add_header = header
			response = urllib2.urlopen( repo_request )
			my_data = json.loads(response.read().decode('utf-8'))
			items = my_data['items']
			for data in items:
				count = count + 1
				repos_data['data'].append(data)
				content_url = data['contents_url'][:-7]
				content_request = urllib2.Request(content_url)
				content_request.add_header = header
				content_response = urllib2.urlopen(content_url)
				content_data = json.loads(content_response.read().decode('utf-8'))
				for content in content_data:
					if content['name'] == 'requirements.txt' or content['name'] == 'requirements-dev.txt':
						requirement_url = content['download_url']
						req = urllib2.Request(requirement_url)
						req.add_header = header
						requirement_response = urllib2.urlopen( req )
						for line in requirement_response:
							package = " ".join(re.findall("^[a-zA-Z]+[0-9]?", line))
							if package != '':
								package_list.append(package)
				if count == 20:
					break
			package_data = Counter(package_list).most_common()		 
			repos_data['package_count'] = package_data
		else:
			raise Exception('no query parameter found in url.Please enter one')

	except Exception , e :
		repos_data['error status'] = 1
		repos_data['error msg'] = str (e)
		
	finally:

		json_data = json.dumps( repos_data , indent = 2)
		return HttpResponse( json_data , content_type = 'application/json')

