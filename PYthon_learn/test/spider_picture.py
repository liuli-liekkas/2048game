import requests
import re
from bs4 import BeautifulSoup
import time

host_url = "http://www.mzitu.com/zipai/"

def get_course_link(url):
    res = requests.get(url)
    print("响应状态码",res.status_code)
    soup = BeautifulSoup(res.text, 'lxml')
    course = soup.select('div[id=comments] > ul > li > div[class=comment-body] > p > img')
    for i in course:
        src = i.get('src')
        pic_name = src.split('/')[-1]
        pic_url = "/Users/hanyan/Documents/github/PYthon_learn/test/{}"
        pic_res = requests.get(src)
        print(pic_res)
        try:
            with open(pic_url.format(pic_name), 'wb') as f:
                print(pic_res.content)
                f.write(pic_res.content)
            print(pic_name,"下载完成")
        except:
            print("图片无法保存，请创建文件夹")
            break
    print("爬取结束 - ", url)


def main():
    res = requests.get("http://www.mzitu.com/zipai/")
    soup = BeautifulSoup(res.text, 'lxml')
    course_link = "http://www.mzitu.com/zipai/comment-page-{}/#comments"
    page = soup.find_all('div', {'class': 'pagenavi-cm'})
    if len(page) < 1:
        print("未获得全部页面")
        return None
    li_num = page[0].find_all('a')
    page_num = 0
    for i in li_num:
        try:
            li_num = int(i.find({'class': 'page-numbers'}).get_txt())
        except:
            li_num = 0
        if li_num > page_num:
            page_num = li_num
    for i in range(1,3):
        print("正在爬取-", course_link.format(i))
        get_course_link(course_link.format(i))
        time.sleep(2)


if __name__ == "__main__":
    main()

