from bs4 import BeautifulSoup as Soup
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
import requests
import selenium.webdriver.support.ui as ui
import time
import random
import csv
from selenium.webdriver.common.action_chains import ActionChains 
import re
import traceback

HEADER  ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/27.0'}

def get_product_link():

    writer = csv.writer(open("bhopal_product_url.csv", "ab+"))
    base_url = "http://www.olx.in/bhopal/?search[photos]=false&page="
    for i in range(1, 600):
        print "Processing page number: " + str(i)
        url =  base_url + str(i)
        html = requests.get(url)
        source = html.text.encode('utf-8')
        matches=re.findall(r'href=\"(.+?)\"',source)
        # items = []
        for match in matches:
            if('www.olx.in/item/' in match):
                writer.writerow([match])


def get_name_mobile(file_path):

    fp = open(file_path, 'rU')
    product_links = fp.readlines();
    writer = csv.writer(open("bhopal.csv", "ab+"))

    for (i, each_product) in enumerate(product_links):
        try:
            product_url = each_product.strip()
            # print (product_url)
            # print (i, product_url)

            html = requests.get(product_url, headers = HEADER)
            source = html.text.encode('utf-8')
            soup = Soup(source,"html.parser")
            userInfo = soup.find("span",attrs={"class":"block color-5 brkword xx-large"})
            name = userInfo.text.encode("utf-8")
            mobile_number_soup = soup.find("strong",attrs={"class":"large lheight20 fnormal  "})
            mobile_number = mobile_number_soup.text.encode("utf-8")
            writer.writerow([name, mobile_number])
            print (i, name, mobile_number)
            # break
        except Exception,e:
            print (e)
            pass


if __name__ == '__main__':

    # get_product_link()
    get_name_mobile('bhopal_product_url.csv')