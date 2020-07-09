#!/usr/bin/python
import sys
from googlesearch import search 
class MyCrawler():
    #Constructor to initalize the variable related to the search 
    #Params:    query,      Type: String,   Usage:variable to search for
    #           g_cleam     Type: List,     Usage: List to store URLs
    #           url         Type: String    Usgae:  Webiste to search for URLS

    def __init__(self):
        self.query=""
        self.g_clean = [] 
        #this is the list we store the search results
        self.url = "".format(self.query)
        #this is the actual query we are going to scrape

    #Setter function for Query
    def set_query(self, name):
        self.query = name
    
    #Getter Function for Query
    def get_query(self,name):
        return self.query

    #Setter Function for URL
    def set_url(self,url):
        self.url = url.format(self.query)

    #Getter Function for URL
    def get_url(self,url):
        return self.url

    #Function to initiate google search based on Query
    def search(self):
        try:
            resultList = search(self.query, tld="com",lang = "en", num=1000,stop=1000,pause=2.0)
            for result in resultList:
                print("URL:"+str(result))
                if result not in self.g_clean:
                    print("LOG: URL added to List")
                    self.g_clean.append(result)
                else:
                    print("LOG: Duplicate URL found!")
                    continue
            return len(self.g_clean)==0
        except Exception as e:
            print(str(e))
            
    #Function to print URL List    
    def printUrl(self):
        try:
            if len(self.g_clean) == 0:
                print("No URLs found")
            else:
                print("Total Results:"+str(len(self.g_clean)))
                for arr in self.g_clean:
                    print(arr)
        except Exception as ex:
            print(str(ex))

    #Function to write URLs to File
    def writeToFile(self,args):
        try:
            filename = args+".txt"
            with open(filename, 'w') as filehandle:
                filehandle.write("\n".join(self.g_clean))
        except Exception as ex:
            print(str(ex))

def main(args):
    crawl = MyCrawler()
    crawl.set_url('https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8')
    crawl.set_query(args)
    if crawl.search()!= True:
        crawl.printUrl()
        crawl.writeToFile(args)
    else:
        print("ERROR: Search failed!")
        
if __name__ == "__main__":
    main(sys.argv[1])
