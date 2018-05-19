import requests
from bs4 import BeautifulSoup
import os
import csv

# downlist  movielist

def get_index(url_num, list_num, num):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    index_urls = 'https://www.' + url_num + '.com/htm/' + list_num + '/'
    if num == 1:
        pass
    else:
        index_urls = index_urls + str(num) + '.htm'
    index_page = requests.get(index_urls, headers=headers)
    index_page.encoding = 'utf-8'
    r = BeautifulSoup(index_page.text, "lxml")
    li = r.find_all('li')
    url_index_list = []
    name_index_list = []
    img_url=[]
    for x in range(len(li)):
        lii = li[x]
        url_index_list.append('https://www.' + str(url_num) + '.com' + lii.a['href'])
        img_url.append(lii.img['src'])
        name_index_list.append(lii.text)
    return url_index_list, name_index_list, img_url



def get_m(url, name):
    vi_name = name[0:-9]
    vi_time = name[-9:]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    vi_page = requests.get(url, headers=headers)
    vi_page.encoding = 'utf-8'
    r = BeautifulSoup(vi_page.text, "lxml")
    dilist = r.find_all('script',type='text/javascript')[5].text[30:-3]
    bianma=dilist.split('/')[-2]
    vi_url = 'http://555.maomixia555.com:888' + dilist
    return vi_name , vi_time , vi_url, bianma


def get_vi(url, name):
    vi_name = name[0:-9]
    vi_time = name[-9:]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    vi_page = requests.get(url, headers=headers)
    vi_page.encoding = 'utf-8'
    r = BeautifulSoup(vi_page.text, "lxml")
    dilist = r.find_all('script',type='text/javascript')[5].text[31:-3]
    bianma1=dilist.split('/')[-1]
    bianma=bianma1.split('.')[0]
    vi_url = 'http://666.maomixia666.com:888' + dilist
    return vi_name , vi_time , vi_url, bianma


def chuanjian():
    with open('D:\\娱乐\\电影_zaixiandongman.csv', 'w', newline='', encoding='gb18030') as f1:
        f_csv = csv.writer(f1)
        f_csv.writerow(['类别', '编码', '名字', '地址', '下载', '封面'])



def cuchun(dir_name, file_name, url_num, list_num, num, leixing):
    a,b,img=get_index(url_num, list_num, num)
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }

    for i in range(len(a)):
        if list_num[0]=='d':
            c, d, e,bianma= get_m(a[i], b[i])
        else:
            c, d, e, bianma = get_vi(a[i], b[i])
        print(list_num)
        xxx=0
        with open(dir_name+'\\'+file_name, 'r',  encoding='gb18030') as f1:
            f1_csv=csv.reader(f1)
            chongfu=[x[1] for x in f1_csv]
            if bianma in chongfu:
                xxx=1
            else:
                pass
        if xxx==1:
            print('重复')
            pass
        else:
            with open(dir_name+'\\'+file_name, 'a', newline='', encoding='gb18030') as f:
                f_csv = csv.writer(f)
                line=[leixing, bianma,c+d,e,0,img[i]]
                f_csv.writerow(line)
                print('成功写入',line[1],line[2])


def dianying(url_num, list_num):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    index_urls = 'https://www.' + url_num + '.com/htm/' + list_num + '/'
    index_page = requests.get(index_urls, headers=headers)
    index_page.encoding = 'utf-8'
    r = BeautifulSoup(index_page.text, "lxml")
    li = r.find('div',class_="pagination")
    page_num=li.find_all('a')[-1]['href'].split('.')[0]
    dir_name='D:\\娱乐'
    if list_num=='downlist1':
        leixing='yazhoudianying'
        file_name='电影_yazhoudianying.csv'
    elif list_num=='downlist2':
        leixing='omeidianying'
        file_name='电影_omeidianying.csv'
    elif list_num=='downlist3':
        leixing='zhifu'
        file_name='电影_zhifu.csv'
    elif list_num=='downlist4':
        leixing='qjll'
        file_name='电影_qjll.csv'
    elif list_num=='downlist7':
        leixing='jingdian'
        file_name='电影_jingdian.csv'
    elif list_num=='downlist6':
        leixing='guochan'
        file_name='电影_guochan.csv'
    elif list_num == 'downlist8':
        leixing = 'dongman'
        file_name = '电影_dongman.csv'
    elif list_num == 'movielist2':
        leixing = 'yazhou'
        file_name = '电影_yazhou.csv'
    elif list_num == 'movielist3':
        leixing = 'oumei'
        file_name = '电影_oumei.csv'
    elif list_num == 'movielist1':
        leixing = 'zhongwen'
        file_name = '电影_zhongwen.csv'
    elif list_num == 'movielist4':
        leixing = 'zaixiandongman'
        file_name = '电影_zaixiandongman.csv'
    else:
        leixing='weizhi'
        file_name = '电影_weizhi.csv'
    for i in range(int(page_num)):
        cuchun(dir_name, file_name, url_num, list_num, i, leixing)


x=['movielist2','movielist3','downlist3','movielist4']
for i in x:
    print('正在写入', i)
    dianying('161cf',i)


