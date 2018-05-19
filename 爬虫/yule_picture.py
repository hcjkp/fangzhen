import requests
from bs4 import BeautifulSoup
import os
import csv


def get_index(url_num, list_num, num):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    index_urls = 'https://www.' + url_num + '.com/htm/piclist' + list_num
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
    for x in range(len(li)):
        lii = li[x]
        url_index_list.append('https://www.' + str(url_num) + '.com' + lii.a['href'])
        name_index_list.append(lii.text)
    return url_index_list, name_index_list


def get_pic(url, name):
    pic_name = name[5:-5]
    name_pic = []
    url_pic = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    pic_page = requests.get(url, headers=headers)
    pic_page.encoding = 'utf-8'
    r = BeautifulSoup(pic_page.text, "lxml")
    imgs = r.find_all('img')
    for x in range(len(imgs)):
        url_pic.append(imgs[x]['src'])
        name_pic.append(pic_name + str(x + 1) + '.jpg')
    return url_pic, name_pic


def get_dir(url, name, pic_dir):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    dir_names = [x for x in os.listdir(pic_dir) if os.path.isdir(pic_dir + '\\' + x)]
    if name in dir_names:
        print('已有该文件夹')
        get_file(pic_dir, url, name)
    else:
        dir_name = pic_dir + '\\' + name
        os.mkdir(dir_name)
        c, d = get_pic(url, name)
        for i in range(len(c)):
            pic = requests.get(c[i], headers=headers).content
            with open(dir_name + '\\' + d[i], 'wb') as f:
                f.write(pic)
            print('     爬取完毕', d[i])
        print('爬取完毕' + name)




def get_file(pic_dir, url, name):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    dir_name = pic_dir + '\\' + name
    files=[x for x in os.listdir(dir_name)]
    num = int(name[-4:-2])
    if len(files) < num:
        a, b = get_pic(url, name)
        for i in range(len(files) , len(a)):
            pic = requests.get(a[i], headers=headers).content
            with open(dir_name + '\\' + b[i], 'wb') as f:
                f.write(pic)
            print('     爬取完毕' + b[i])
        print('爬取完毕', name)
    else:
        pass


def inf_in():   #输入必要信息 页码 和 类别


    while True:   # 输入类别
        name = input('请输入类别 tou ya ou mei qing shou')
        if name == 'tou':
            index_num = '1/'
            break
        elif name == 'ya':
            index_num = '2/'
            break
        elif name == 'ou':
            index_num = '3/'
            break
        elif name == 'mei':
            index_num = '4/'
            break
        elif name == 'qing':
            index_num = '6/'
            break
        elif name == 'shou':
            index_num = '7/'
            break
        else:
            print('错误，请输入正确代码')

    while True:
        num1 = input('请输入起始页码')
        num2 = input('请输入截止页码')
        if int(num1) < 1 or int(num2) < 1:
            print('输入一个正数')
        elif int(num1) <= int(num2):
            break

    while True:
        url_num = input('请输入网址中的数字')
        try:
            x = requests.get('http://www.' + url_num + '.com/htm/index.htm')
            x.encoding = 'utf-8'
            b = BeautifulSoup(x.text, 'lxml')
            yan = b.find('li').text
            if yan == '在线电影':
                break
            else:
                pass
        except AttributeError as e:
            print('输入错误', e)
    return index_num, int(num1), int(num2), url_num, name


def out():
    list_num, n1, n2, url_inf, name = inf_in()
    a = 'd:\\娱乐\\picture'
    dir_list = [x for x in os.listdir(a) if os.path.isdir(a + '\\' + x)]
    for x in range(n1, n2 + 1):
        for i in range(len(dir_list)):
            file_list = [t for t in os.listdir(a + '\\' + dir_list[i])]
            if len(file_list) < 30:
                dir_name = a + '\\' + dir_list[i]
            else:
                pass
        os.mkdir(a + '\\' + str(len(dir_list)))
        dir_name = a + '\\' + str(len(dir_list))
        url_index_list, name_index_list = get_index(url_inf, list_num, x)
        for i in range(len(url_index_list)):
            get_dir(url_index_list[i], name_index_list[i], dir_name)
