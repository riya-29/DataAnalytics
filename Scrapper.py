# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 19:44:21 2022

@author: Riya
"""
 
import pandas as pd
import requests
from selenium import webdriver

url = 'https://m.dailyhunt.in/news/india/english/news?mode=pwa&action=click'
response = requests.get(url)
data = {}
Stories = {"Headline":[],
           "Time":[],
           "Content":[]}

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path = r'D:\chromedriver',options=options)

browser.get(url)
text=browser.page_source

for i in range(1,20):
    try:
        headline = text.split('figcaption class=')[i].split('<h2 class=')[1].split('">"')[0].split('</h2')[0]
        t = text.split('class="shareWrpTxt">')[i].split('</li>')[0]
        content = text.split('<p style')[i].split('</p>')[0].split(">")[1].split("<")[0]
        
        if len(t) < 5 and len(content) > 30:    
            print("_____________________________________")
            headline = headline.split('">')[1]
            t = t+" ago"
            print("\nHeadline: ", headline)
            print("\nTime: ", t)
            print("\nContent: ", content)
            
            Stories['Headline'].append(headline)
            Stories['Time'].append(t)
            Stories['Content'].append(content)
            print("_____________________________________")
    except:
        print("Err")
        pass
df =pd.DataFrame(Stories)
df.to_csv("News.csv")




