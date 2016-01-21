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

  def __init__(self,query):

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

    pprint.pprint(res)

  def research_paper_search(self):

    #service = build("customsearch","v1",
    #         developerKey = "AIzaSyCGD8RWG9IAkKw57aHJM2NVTO2nl72CKus")

    paper_query = self.query

    res = self.service.cse().list(
          q= paper_query,
          cx= "016910633958041350436:dgzalhpaidu",
          num = self.max_limits,

          ).execute()


    pprint.pprint(res)


if __name__ == '__main__':
  s = Search("MachineLearning")
  s.research_paper_search()