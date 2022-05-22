import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession
from html.parser import HTMLParser
import os


def getCrimes():
  def urlsource(url):
    try:
      session = HTMLSession()
      response = session.get(url)
      return response

    except requests.exceptions.RequestException as e:
      print(e)


  html_list = []
  link = "https://www.wrps.on.ca/Modules/NewsIncidents/search.aspx?feedId=73a5e2dc-45fb-425f-96b9-d575355f7d4d&page="
  for i in range(100):
    try:
      url = urllib.request.urlopen(link+str(i+1))
      html = url.read()
      if str(html).count("No Results Found")>=2:
        break
      html_list.append(html)
    except urllib.error.HTTPError as e:
      with open('pg.txt','w') as f:
        f.write(str(e))
      pass

  global temp
  temp = []
  rawdata = []
  class coolHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
      pass
    def handle_data(self, data):
      if len(data) >= 30:
        temp.append(data)
    def handle_endtage(self,tag,attrs): 
      pass


  parser = coolHTMLParser()
  ix = 0
  for html in html_list:
    ix+=1
    parser.feed(str(html))
    rawdata += [temp]

  filtereddata = []
  temp = []
  for article in rawdata:
    for datapiece in article:
      if "Location:" in datapiece:
        useless,datapiece = datapiece.split(":")
        temp.append(datapiece.lstrip("\\n").strip())
        filtereddata += [temp]
        temp = []
      elif "Incident Date:" in datapiece: 
        datapiece = datapiece.replace("Incident Date:","")
        temp.append(datapiece.lstrip("\\n").strip())
      elif "WA" in datapiece:
        temp.append(datapiece.lstrip("\\n").strip())

  return filtereddata