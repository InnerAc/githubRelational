#!/usr/bin/python
#encoding=utf-8
# @innerac
import urllib2
import urllib
import string
import json
import sys
import re
import os
import static
import sqlite3
from bs4 import BeautifulSoup


def getHtml(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    page = urllib2.urlopen(req)
    html = page.read()
    return html

def ddu(tmp):
    return eval(repr(tmp)[1:])

def analysisDetails(lis):
    dic = {}
    for li in lis:
        liType = li.find('span')['class'][1]
        if(liType == static.ORGANIZATION):
            tmp =  li.contents[1]
            art = tmp.string
            if(type(art) == type(None)):
                tmp = li.contents[3].string
            dic['organization'] = eval(repr(tmp)[1:])
        elif(liType == static.LOCATION):
            tmp =  li.contents[1]
            dic['location'] = eval(repr(tmp)[1:])
        elif(liType == static.MAIL):
            tmp =  li.find('a').string
            dic['mail'] = eval(repr(tmp)[1:])
        elif(liType == static.LINK):
            tmp = li.find('a').string
            dic['link'] = eval(repr(tmp)[1:])
        elif(liType == static.CLOCK):
            tmp =  li.find('time').string
            dic['clock'] = eval(repr(tmp)[1:])
    return dic
def analysiStats(As):
    dic = {}
    for a in As:
        stat,num = ddu(a.span.string), ddu(a.strong.string)
        if stat == 'Follower':
            stat = 'Followers'
        dic[stat] = num
    return dic
def findNext(lis):
    sets = []
    for li in lis:
        name = li.find('div').find('h3').find('span').find('a')['href'][1:].lower().replace(' ','')
        sets.append(name)
    return sets
def save(page,files,types):
    f = open(files,types)
    f.write(page+'\n')
    f.close()

def insert(maps):
    conn = sqlite3.connect('person.db')
    sqlInsert = "INSERT INTO person (url,name,organization,location,mail,link,clock,star,following,follower,friend) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(maps['url'],maps['name'],maps['organization'],maps['location'],maps['mail'],maps['link'],maps['clock'],maps['Starred'],maps['Following'],maps['Followers'],maps['friends'])
    conn.execute(sqlInsert);
    conn.commit()
    conn.close()

def start(name):
    
    url1 = 'https://github.com/{}?tab=repositories'.format(name)
    url2 = 'https://github.com/{}/followers'.format(name)
    url3 = 'https://github.com/{}/following'.format(name)
    
    # get details    
    html = getHtml(url1)
    soup = BeautifulSoup(html)
    person = {'url':'','name':'','organization':'','location':'','mail':'','link':'','clock':'','Following':'','Follower':'','friends':'','Starred':''}
    VcardDetails = {'url':name} 
    name = soup.find('span',{'class','vcard-fullname'}).string
    if(type(name) == type(None)):
        name = soup.find('span',{'class','vcard-username'}).string
    print name
    VcardDetails['name'] = name
    
    ul = soup.find('ul',{'class','vcard-details'})
    lis = ul.findAll('li')
    VcardDetails.update(analysisDetails(lis))
    div = soup.find('div',{'class','vcard-stats'})
    As = div.findAll('a')
    VcardDetails.update(analysiStats(As))

    person.update(VcardDetails)    
    # info = json.dumps(VcardDetails)
    # save(info,'info.json','a')
    
    # get next
    html = getHtml(url2)
    soup = BeautifulSoup(html)
    ol = soup.find('ol')
    if(type(ol) != type(None)):
        lis = ol.findAll('li')
        followers = set(findNext(lis))
    
    html = getHtml(url3)
    soup = BeautifulSoup(html)
    ol = soup.find('ol')
    if(type(ol) != type(None)):
        lis = ol.findAll('li')
        following = set(findNext(lis))
    friend = followers & following
    person['friends'] = ','.join(k for k in friend)
    insert(person)
    nexts = followers | following
    
    return nexts
if __name__ == '__main__':
    name = 'KevinSawicki'
    start(name)
