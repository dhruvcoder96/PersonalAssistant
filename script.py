from bs4 import BeautifulSoup as bs
from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route("/")
def home():
    quoterespons = requests.get("http://www.eduro.com/")
    qc = quoterespons.content
    soup = bs(qc,"html.parser")
    finder1 = soup.find("div",{"class":"singlemeta"})
    quote = finder1.find("p").text
    authorname = finder1.find("p",{"class":"author"}).text.replace('\xa0','').replace('\n','')
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    c1 = r.json()
    url1="http://api.openweathermap.org/data/2.5/weather?lat="+str(c1['latitude'])+"&lon="+str(c1['longitude'])+"&appid=e107f5f0f499deaa5b9e63a995411a73&units=metric"
    r1 = requests.get(url1)
    d1=r1.json()
    r = requests.get("https://newsapi.org/v1/articles?source=abc-news-au&sortBy=top&apiKey=229d96014fbd44219f9382a500c4c0fc")
    r12=r.json()
    return render_template("home.html",quote=quote,authorname=authorname,datatemp=d1,r12=r12)

if __name__=="__main__":
    app.run(debug=True)
