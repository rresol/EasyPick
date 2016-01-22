__author__ = 'rresol'
__email__  = 'shashank.kumar.apc13@itbhu.ac.in'


#To search for the related courses on udacity and coursera and returning the response

import json
import urllib2


#Integrating Both API's
def search(query):
	response = ''
	coursera_response = coursera(query)
	udacity_response  = udacity(query)
	response += 'The available courses on coursera are:\n ' +coursera_response+ ' \nThe available courses on udacity are: \n' + udacity_response
	print response
	return response


#Implementing Coursera API
def coursera(query):
	response = urllib2.urlopen('https://api.coursera.org/api/courses.v1?ids=v1-3,Gtv4Xb1-EeS-ViIACwYKVQ&fields=name,slug')
	f = open('coursera.json','w')
	f.write(response.read())
	f.close()

	catalog = json.load(open('coursera.json'))['elements']
	coursera_response = ''
	for course in catalog:
		if query.lower() in course['name'].lower():
			coursera_response += course['name'] + ": " 

			ur = 'https://www.coursera.org/learn/'+course['slug']
			coursera_response += ur + '\nIf the link does not work then try this\n' +'https://www.coursera.org/specializations/' + course['slug']
			
			#print ur
			#u = urllib2.urlopen('http://www.coursera.org/learn/'+course['slug'])
			
			#print ur
			
			#if u.getcode() == 200:
			#	coursera_response += ur
			#	print ur
			
			#else:
			#	ur = 'https://www.coursera.org/specializations/' + course['slug']
			#	u = urllib2.urlopen(ur)
			#	if u.getcode() == 200:
			#		coursera_response += ur
			#	else:
			#		coursera_response += " Sorry for the inconvenience but we can't extract the url of the course due to API limitations."		
	
	return coursera_response

#Implementing Udacity API
def udacity(query):
	response = urllib2.urlopen('https://udacity.com/public-api/v0/courses')
	f = open('udacity.json','w')
	f.write(response.read())
	f.close()


	catalog = json.load(open('udacity.json'))['courses']
	udacity_response =''

	for course in catalog:
		if query.lower() in course['title'].lower():
			udacity_response += course['title'] + ": " + course['homepage'] + '\n'


	return udacity_response

if __name__ == '__main__':
	search('machine')