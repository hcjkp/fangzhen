import requests
import os
import csv
from bs4 import BeautifulSoup
import yule_picture


def get_data(pic_dir):
    csv_name = 'd:\\娱乐\\picture.csv'
    if 'picture.csv' in os.listdir(pic_dir):
        pass
    else:
        with open(csv_name, 'w', newline='',encoding='gb18030') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(['类别', '文件夹名字', '名字', '地址', '下载'])
    with open(csv_name, 'r',encoding='gb18030')as f1:
        f_read = csv.reader(f1)
        d = [x for x in f_read]
        print(d)
    with open(csv_name, 'a', encoding='gb18030', newline='') as f:
        f_csv = csv.writer(f)

        list_num, n1, n2, url_inf, name = yule_picture.inf_in()
        for x in range(n1, n2 + 1):
            url_index_list, name_index_list = yule_picture.get_index(url_inf, list_num, x)
            for i in range(len(url_index_list)):
                a, b = yule_picture.get_pic(url_index_list[i], name_index_list[i])
                for t in range(len(a)):
                    c = [name, name_index_list[i], b[t], a[t], '0']

                        #if c in d:
                            #print('已有', c)
                        #else:
                        #f_csv.writerow(c)

                        #print('正在写入',name_index_list[i])
get_data('d:\\娱乐\\picture')
