__author__ = 'rresol'
__email__  =  'shashank.kumar.apc13@iitbhu.ac.in'


'''
Searching the contents related to query using google custom
search
'''

import pprint

from googleapiclient.discovery import build

def booksearch(query):
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyCGD8RWG9IAkKw57aHJM2NVTO2nl72CKus")

  query += "books"
  res = service.cse().list(
      q=query,
      cx='016910633958041350436:wrwlxthfvui',
    ).execute()
  pprint.pprint(res)




if __name__=='__main__':
	booksearch()