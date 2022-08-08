import requests, bs4
import pandas as pd
def movie1():
    url = 'https://movies.yahoo.com.tw/movie_thisweek.html'     # 本周新片的網址
    moviehtml = requests.get(url)
    objSoup = bs4.BeautifulSoup(moviehtml.text, 'lxml')         # 取得新片網址的HTML
    content = []
    movieNum = 0
    items = objSoup.find_all('div', 'release_info')             # 新片在此資料區間
    for item in items:

        cName = item.find('div', 'release_movie_name').a.text.strip()   # 中文片名
        eName = item.find('div', 'en').a.text.strip()                   # 英文片名
        rTime = item.find('div', 'release_movie_time')          # 上映日期
        level = item.find('div', 'leveltext').span.text.strip() # 期待度
        txt = item.find('div', 'release_text').text.strip()     # 內容摘要
        movieNum += 1
        content.append( "新片編號"+str(movieNum) + '\n' +
                        "中文片名"+cName    + '\n' +
                        "英文片名"+eName    + '\n' +
                        rTime.text+'\n' +
                        "期待度" + level + '\n' +
                        "內容摘要" + txt )

    moviemessage= '\n\n'.join(content)
    return moviemessage


def stock1():

    namelist=[]
    priceopen_list=[]
    priceclose_list=[]
    differenceprice_list=[]
    content=[]

    url='https://www.twse.com.tw/exchangeReport/MI_INDEX?response=html&date=20170601&type=ALLBUT0999'
    response= requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    soup1=soup.find_all('table')[8].tbody.find_all('tr')

    for a in soup1:
        name=a.find_all('td')[1].text
        price1=a.find_all('td')[5].text
        price7=a.find_all('td')[7]
        difference1=a.find_all('td')[10]
        content.append("a"+str(name)+"b"+str(price1))
    test=content  
    return test


def stock3(stock):
  
    url='https://tw.stock.yahoo.com/quote/'+stock
    response=requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    name1=soup.find('h1').text
    name1
    price1=soup.find('div',class_="D(f) Ai(fe) Mb(4px)")
    price2=price1.find('span').text
    price2

    try:
        difference = soup.find('span', class_="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-down)").text
        s = '-'
        difference3 = s + difference
    except:
        difference1 = soup.find('span', class_="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-up)").text
        s = "+"
        difference3 = s + difference1

    content = "name:" + name1 + "\n" + "price2:" + price2 + "\n" +"difference:" + difference3

    return content
