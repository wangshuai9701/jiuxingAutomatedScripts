#encoding = utf-8
import time
# import urllib2
import json
import unittest
from unittest import main

import CodeDemo #导入第三方识别验证码py文件包
import random  #s随机数包
import pytesseract      # 解析验证码包pip.exe install pytesseract
from PIL import Image   # pip.exe install Pillow截图
from PIL import ImageEnhance
from selenium import webdriver  # 导入webdriver包
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #找页面元素
from selenium.webdriver.common.by import By




class Operations():
    def nihao(self):
        global driver
        driver = webdriver.Chrome()
    def getCode(self,imagPath,imagSavePath):  #####裁剪图片，获取验证码图片
        driver.save_screenshot(imagPath)
        time.sleep(1)
        code_img = driver.find_element_by_class_name("codeSrc")
        left = code_img.location['x']
        top = code_img.location['y']
        right = code_img.size['width'] + left
        height = code_img.size['height'] + top
        im = Image.open(imagPath)
        img = im.crop((left, top, right, height))
        img.save(imagSavePath)

    def parseVerificationCode(self, imagSavePath):  #####对验证码处理，并调第三方验证码识别方法
        # global code1
        imag = Image.open(imagSavePath)
        time.sleep(1)
        # imag = imag.convert('RGBA')
        #
        # enhancer = ImageEnhance.Color(imag)
        #
        # enhancer = enhancer.enhance(0)
        #
        # enhancer = ImageEnhance.Brightness(enhancer)
        #
        # enhancer = enhancer.enhance(2)
        #
        # enhancer = ImageEnhance.Contrast(enhancer)
        #
        # enhancer = enhancer.enhance(8)
        #
        # enhancer = ImageEnhance.Sharpness(enhancer)
        #
        # imag = enhancer.enhance(20)
        imag = imag.convert('RGBA')  # 转换模式：L | RGB
        imag = imag.convert('L')  # 转换模式：L | RGB
        imag = ImageEnhance.Contrast(imag)  # 增强对比度
        imag = imag.enhance(2.0)  # 增加饱和度
        # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
        # threshold = 200

        # table = []
        # for i in range(256):
        #     if i < threshold:
        #         table.append(0)
        #     else:
        #         table.append(1)
        # imag = imag.point(table, '1')

        imag.save(imagSavePath)
        # time.sleep(1)
        # imag = Image.open(imagSavePath)
        time.sleep(1)
        img_path = imagSavePath
        img = Image.open(img_path)
        self.code1 = CodeDemo.base64_api("wangmoumou", "gjil668kps", img=img)
        print(self.code1)
        # 注释的是python自带的识别图片的语句
        # code = pytesseract.image_to_string(imag)
        # time.sleep(2)
        # code1 = ''.join(code.split())
        # time.sleep(2)
