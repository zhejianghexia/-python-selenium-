#在风之动漫网上下载海贼王，输入需要下载的章节，将漫画下载的本地
#实现思路：
# 1 海贼王的漫画目录链接是：https://www.fzdm.com/manhua/02/
# 2 第X话的漫画。连接是https://www.fzdm.com/manhua/02/X/，例如，924话链接是https://www.fzdm.com/manhua/02/924/
# 3 第X话漫画中，第一页的链接是：https://www.fzdm.com/manhua/02/924/，第二页是https://www.fzdm.com/manhua/02/924/index_1.html
#    第三页是https://www.fzdm.com/manhua/02/924/index_2.html，经尝试，index_0.html就是第一页的链接
#利用迭代，可以获得一到最后一页的图片，但是无法准确知道那一页是最后一页，利用try..exception..函数，抛出异常，并结束。
#因为，图片的链接使用js脚本加载的，无法直接在静态网页中获得http链接，所以使用selenium定位图片位置，然后使用get_attribute('src')
#获得图片的链接
#之后用resquests请求，将图片下载的本地
#


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests
import time
import os
import sys
def manhua_download():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')  # 关闭自动化程序运行的提示
    # option.add_argument('--headless')      #隐藏浏览器窗口
    driver=webdriver.Chrome(options=option)
    #上面三行可以使得浏览器不弹出自动化测试的拦截窗口
    x=input("请问要下载第几话？")
    url=os.path.join('https://manhua.fzdm.com/2/',x)
    # 创建章节目录
    dirname = '第' + str(x) + '话'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print('文件夹创建完毕')
    for i in range(30):

        index='index_'+str(i)+'.html'
        final_url=os.path.join(url,index)
        driver.get(final_url)
        try:
            img_path = driver.find_element_by_xpath(".//img[@id='mhpic']")
        except NoSuchElementException:
            print('下载完毕')
            driver.quit()
            sys.exit()              #捕获异常后退出程序
        img_url = img_path.get_attribute('src')  # get_attribute('src') 获取src内的内容
        print(img_url)
        time.sleep(0.1)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}
        response = requests.get(img_url,headers=headers)
        image_name=dirname+'/'+str(i+1)+'.jpg'   #实现下载的图片存到指定的文件夹的功能
        with open(image_name,'wb') as f:
            f.write(response.content)
            print('第'+str(i+1)+'页已下载')

manhua_download()








