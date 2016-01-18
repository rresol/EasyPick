__author__ = 'rresol'

'''
This module is particularly written to search fof the courses available on mit.edu . Web Scraping has been used to 
get the response . Web Scraping is illegal on most of the web sites . So , try using it carefully.
'''
import requests
from bs4 import BeautifulSoup

def mit_courses(query):

	
	url = 	"http://search.mit.edu/search?site=ocw&client=mit&getfields=*&" +\
        	"output=xml_no_dtd&proxystylesheet=http%3A%2F%2Focw.mit.edu%2Fsearch%2Fgoogle-ocw" +\
            ".xsl&requiredfields=WT%252Ecg_s%3ACourse+Home|WT%252Ecg_s%3AResource+Home&" +\
            "sectionlimit=WT%252Ecg_s%3ACourse+Home|WT%252Ecg_s%3AResource+Home&as_dt=i&oe=" + \
            "utf-8&departmentName=web&filter=0&courseName=&q="
	
	
	url += query
	url +=  "&btnG.x=0&btnG.y=0"
	r   =   requests.get(url)
	
	#print r.encoding (utf-8)
	soup = BeautifulSoup(r.content,"lxml",from_encoding = "utf-8")
	
	courses = soup.find_all("p")
	counter = 1  # A measure to tackle the first three links of the web page.
	course_data = {}

	for course in courses:
	
		links = course.find_all("a")
		if counter >=3 and counter <=13 :
	
			for link in links:
	
				value = link.get("href")
				key = link.text
				key = key.encode('ascii','ignore') #unicoded earlier
	
				#print type(key)
				#print type(value)
				#print key + ": " + value
 	
 				course_data[key] = value
		counter +=1 
	

	#print course_data
	return course_data

if __name__=='__main__':
	mit_courses("Machine")