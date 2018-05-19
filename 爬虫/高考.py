import requests
from bs4 import BeautifulSoup


def get_num():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    a=requests.get('http://wl.eywedu.net/gaokao/List/List_633.html',headers=headers)
    a.encoding='gbk'
    soup=BeautifulSoup(a.text,'lxml')
    tr=soup.find_all(valign='top',height='100')
    href=[]
    for i in range(1,len(tr)):
        print(tr[i])


    print(tr)
get_num()