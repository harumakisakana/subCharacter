from bs4 import BeautifulSoup
import requests

def readingHTML(url,target):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    result=soup.find(text=target).parent.parent.parent.parent
    return result
