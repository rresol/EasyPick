__author__ = 'resol'
__email__  = 'shashank.kumar.apc13@itbhu.ac.in'


import pprint

from apiclient.discovery import build

class Search:

#Google Custom Search Engine to Search for books and  research paper.
#Two different Search engines have been used . one of them searches for 
#books on Amazon Web Store while the other one exclusively searches for 
#research papers using google scholar. 
#Query is what you want to google .

  def __init__(self,query,max_limits=5):

    self.query = query
    self.service = build("customsearch","v1",
                   developerKey = "AIzaSyCGD8RWG9IAkKw57aHJM2NVTO2nl72CKus") #Use your own developer Key dont use mine 
                                                                            #Even if you did it will expire ...lol...
    self.max_limits = 5

  def book_search(self):

    #This functionality searches for books available on amazon web store.

    book_query = self.query
    book_query += "books"
  
    res = self.service.cse().list(
          q = book_query,
          cx= "016910633958041350436:hh2ahxc5z8e",                    #Have your own search engine not mine.
          num = self.max_limits,
          ).execute()

    research_data = 'The Best rated books based on your search are : \n'
    unicode_data = res['items']
    for d in unicode_data:

      book_data += d['link'].encode("ascii","ignore") + '\n'
      
      #print book_data
      return book_data
    
  def research_paper_search(self):

    paper_query = self.query

    res = self.service.cse().list(
          q= paper_query,
          cx= "016910633958041350436:dgzalhpaidu",
          num = self.max_limits+1,

          ).execute()
    
    research_data = 'Most Cited Researh Papers based on your search are : \n'
    unicode_data = res['items'][1:]
    for d in unicode_data:

      try:
        data += d['pagemap']['itemlist'][0]['itemlistelement'].encode("ascii","ignore").split(',')[0] + ":   "
      except:
        research_data += 'Title not Found here is the link  :   '
      research_data += d['formattedUrl'].encode("ascii","ignore") + '\n'
      
    #print research_data
    #print res['items'][1]['kind'].encode("ascii","ignore")
    #pprint.pprint(res)
    return research_data
    


if __name__ == '__main__':
  s = Search("MachineLearning")
  result = s.research_paper_search()
  print result