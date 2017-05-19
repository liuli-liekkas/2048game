import requests
import re
from bs4 import BeautifulSoup
import time
import sqlite3

host_url = "http://www.shiyanlou.com{}"
base_url = "/Users/hanyan/Documents/github/PYthon_learn/test/spider.sqlite3.db"
table_name = "course_info"


def create_table():
    sql3_db = sqlite3.connect(base_url)
    create_sql = "create table {} (url VARCHAR(1024), title VARCHAR(256), teacher VARCHAR(128),study_num INT, tag VARCHAR(256),types VARCHAR(256), info VARCHAR(1024),tests_name VARCHAR(1024))".format(
        table_name)
    try:
        sql3_db.execute(create_sql)
    except:
        return False
    sql3_db.close()
    return True


def query(title):
    sql3_db = sqlite3.connect(base_url)
    query_sql = "select * from {} WHERE title = '{}'".format(table_name, title)
    cu = sql3_db.cursor()
    cu.execute(query_sql)
    record_list = cu.fetchall()
    if len(record_list) > 0:
        return True
    else:
        return False
    return False


def insert_or_update_data(url, title, teacher, study_num, tag, types, info, tests_name):
    create_table()
    if query(title):
        sql3_db = sqlite3.connect(base_url)
        update_sql = "update {} set study_num={}, info='{}', tests_name='{}', url='{}' WHERE title='{}'".format(
            table_name, study_num, info, tests_name, url, title)
        try:
            sql3_db.execute(update_sql)
            sql3_db.commit()
        except:
            return False
        sql3_db.close()
        return True
    else:
        sql3_db = sqlite3.connect(base_url)
        insert_sql = "insert into {} (url, title, teacher, study_num, tag, types, info, tests_name) VALUES('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}')".format(
            table_name, url, title, teacher, study_num, tag, types, info, tests_name)
        try:
            sql3_db.execute(insert_sql)
            sql3_db.commit()
        except:
            return False
        sql3_db.close()
        return True
    return False


def parse_content(url, title, tag, study_num):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    type_list = soup.select('ol[class=breadcrumb] > li > a')
    types = []
    for i in type_list:
        if type_list.index(i) != 0 and type_list.index(i) != len(type_list) - 1:
            types.append(i.get_text())
    info = soup.find('div', {'class': 'course-infobox-content'})
    try:
        info = info.find('p').get_text()
    except:
        info = "无介绍"
    teacher = soup.find('div', {'class': 'name'})
    try:
        teacher = teacher.find('strong').get_text()
    except:
        teacher = "匿名"
    labs = soup.find('div', {'id': 'labs'})
    test_list = labs.find_all('div', {'class': 'lab-item'})
    tests_name = []
    for i in test_list:
        name = i.find('div', {'class': 'lab-item-title'}).get_text()
        tests_name.append(name)
    print(url, insert_or_update_data(url, title, teacher, study_num, tag, '-'.join(types), info, '-'.join(tests_name)))


def get_course_link(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    course = soup.find_all('div', {'class': 'col-md-4', 'class': 'col-sm-6', 'class': 'course'})
    for i in course:
        href = i.find('a', {'class': 'course-box'}).get('href')
        title = i.find('div', {'class': 'course-name'}).get_text()
        study_people = i.find('span', {'class': 'course-per-num', 'class': 'pull-left'}).get_text()
        study_people = re.sub("\D", "", study_people)
        try:
            tag = i.find('span', {'class': 'course-per-num', 'class': 'pull-right'}).get_text()
        except:
            tag = "普通课程"
        parse_content(url=host_url.format(href), title=title, tag=tag, study_num=study_people)
        time.sleep(0.5)


def main():
    res = requests.get('https://www.shiyanlou.com/courses/')
    soup = BeautifulSoup(res.text, 'lxml')
    course_link = "https://www.shiyanlou.com/courses/?course_type=all&tag=all&fee=all&page={}"
    page = soup.find_all('ul', {'class': 'pagination'})
    if len(page) < 1:
        print('未获得全部页面')
        return None
    li_num = page[0].find_all('li')
    page_num = 0
    for i in li_num:
        try:
            li_num = int(i.find('a').get_text())
        except:
            li_num = 0
        if li_num > page_num:
            page_num = li_num
    for i in range(1, page_num + 1):
        get_course_link(course_link.format(i))


if __name__ == "__main__":
    main()
