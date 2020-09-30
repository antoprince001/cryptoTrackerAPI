from flask import Flask,request
import urllib.request
from bs4 import BeautifulSoup
from newsapi import NewsApiClient

app = Flask(__name__)

newsapi_apikey = '01dd9bdbb831421da729c605300ec9e2'
newsapi = NewsApiClient(api_key=newsapi_apikey)

@app.route('/')
def hello_world():
        return 'Crypto Tracker'

#sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg sc-1mty1jv-2 dtichT
@app.route('/bitcoin/price')
def bitPrice():
    url = 'https://www.blockchain.com/explorer'
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage, 'lxml')
    output = soup.find_all('span',{"class": "sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg sc-1mty1jv-2 dtichT"})
    #output = soup.find_all('span',{"class": "sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg sc-1mty1jv-2 dtichT"})

    return str(output)


@app.route('/ethereum/price')
def ethPrice():
    url = 'https://www.blockchain.com/prices'
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage, 'lxml')
    output = soup.find_all('span',{"class": "sc-1ryi78w-0 hxcrTa sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg"})
    return str(output)


@app.route('/blockchain/news')
def blockNews():
    #top_headlines = newsapi.get_top_headlines(sources='TechCrunch')
    top_headlines=newsapi.get_everything(q='blockchain',page=1)
    return top_headlines




@app.route('/blockchain/newsByName')
def blockNewsByName():
    tag = request.args.get('topic')
    top_headlines=newsapi.get_everything(q=tag,page=1)
    return top_headlines


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
