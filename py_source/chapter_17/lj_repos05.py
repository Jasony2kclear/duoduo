#自动登陆为止
import time
import json
import random
import os
import platform
import pandas as pd
from selenium import webdriver
from selenium.common import exceptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq

class VisaOnline:
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.get_user_info()
        if self.is_window():
            options.binary_location = self.chromepath
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        options.add_experimental_option("useAutomationExtension",False)
        options.add_experimental_option("prefs",{"prfile.managed_default_content_setting.images":2})
        self.browser = webdriver.Chrome(options = options,executable_path=self.get_chromedriver_exe_path())
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
            "source":"""
            Object.defineProperty(navigator,'webdriver',{
                get: () => undefined
            })
            """
        })

        self.wait = WebDriverWait(self.browser,10)
        self.loginurl = "https://www.visaonline.com"


    # 从config.jason中读取相关配置信息
    def get_user_info(self):
        with open("config.jason","r",encoding="utf-8") as f:
            config=json.load(f)
        self.username = config["username"]
        self.password = config["password"]
        self.chromepath = config["chromepath"]

    #判断是否是windows
    def is_window(self):
        return platform.system().lower() == "windows" 
        
    # 得到不同平台的Chromedriver的路径
    def get_chromedriver_exe_path(self):
        ret = "./bin/mac/chromedriver"
        if self.is_window():
            ret = "c:/temp/chromedriver.exe"
        return ret

    def login(self):
        self.browser.get(self.loginurl)
        try:
            #找到用户名输入框并且输入
            username_input = self.wait.until(EC.presence_of_element_located((By.ID,"txtUsername")))
            username_input.send_keys(self.username)
            #找到密码输入框并且输入
            password_input = self.wait.until(EC.presence_of_element_located((By.ID,"txtPd")))
            password_input.send_keys(self.password)
            #找到登陆按钮并点击
            login_button = self.wait.until(EC.presence_of_element_located((By.ID,"btnLogin")))
            login_button.click()
            #找到名字标签并且打印内容
            taobao_name_tag = self.wait.until(EC.presence_of_element_located((By.ID,"spanpersonaName")))
            print(f"登陆成功：{taobao_name_tag.text}")
        except exception as e:
            print(e)
            self.browser.close()
            print('登陆失败!')

    #登陆后找到目标地点
    def GogoPoint(self):
        sleep_time = random.randint(1,5)
        time.sleep(sleep_time)
        VisaRiskM = self.wait.until(EC.presence_of_element_located((By.ID,"VRMEXT")))
        VisaRiskM.click()
        #self.browser.get('https://vrm-ext.visaonline.com/secure/app/case-mgmt/queues')
        #sleep_time = random.randint(1,5)
        #time.sleep(sleep_time)
        #self.browser.get('https://vrm-ext.visaonline.com/secure/app/reports')
        #sleep_time = random.randint(1,5)
        #time.sleep(sleep_time)
        time.sleep(10)
        ToRun = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'li.visa-ui-linktabs--item.link-parent.router-link-active.visa-ui-state--active')))
        #ToRun = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#vrm-nav reports')))
#        ToRun = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.visa-ui-viewport li.visa-ui-linktabs--item link-parent router-link-active visa-ui-state--active a.nav-link')))
        ToRun.click()
        time.sleep(10)

if __name__ == "__main__":
    spider = VisaOnline()
    spider.login()
    spider.GogoPoint()
