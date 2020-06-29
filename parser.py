from selenium import webdriver
import requests 
from bs4 import BeautifulSoup
import os
import time
from PIL import Image
import threading

   
next_page=True
next_chapter=True

os.chdir("C:/Users/colin.huang/Desktop/parse/slam dunk")

chromedriver = "C:/Users/colin.huang/Desktop/parse/chromedriver"
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.manhuaren.com/m9859/')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="lb-win"]/div/a[2]/img').click() # close ad

index=1
chapter=25

path="C:/Users/colin.huang/Desktop/parse/slam dunk"

while next_chapter:
    os.chdir("C:/Users/colin.huang/Desktop/parse/slam dunk")
    os.mkdir("slam_dunk_{}".format(chapter))
    os.chdir("slam_dunk_{}".format(chapter))
    while next_page:

        try:

            url_image=driver.find_element_by_xpath("//div[@class='view-main-1 readForm']/img").get_attribute("src")

            res = requests.get(url_image)

            with open('slam_dunk_{0}_{1}.png'.format(chapter,index), 'wb') as f:

                f.write(res.content)

            print('第%d章_%d張圖片下載完成' % (chapter,index))

            driver.find_element_by_xpath('/html/body/ul/li[3]/a').click()
            time.sleep(2.5)
            index+=1
        except:
            print("This Chapter{0} is over".format(chapter))
            next_page=False
            driver.find_element_by_xpath('/html/body/div[7]/a[2]').click() # jump to next chapter
            chapter+=1
            index=1

    next_page=True

   
# convert images to pdf
os.chdir("C:/Users/colin.huang/Desktop/parse/slam dunk/")

for l in sorted(os.listdir(), key=os.path.getctime):
    dirname=os.path.join("C:/Users/colin.huang/Desktop/parse/slam dunk/",l)
    os.chdir(dirname)    
    with open('{0}.pdf'.format(l),"wb") as f:     
        imgs = []
        for fname in sorted(os.listdir(dirname), key=os.path.getctime):
            if not fname.endswith(".png"):
                continue
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
            print(l+'------'+fname)
        f.write(img2pdf.convert(imgs))
