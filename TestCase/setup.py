import requests
import hashlib
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# import time
'''
def get_cookie(phone,pwd):
    ch_options = Options()
    # 配置Chrome为无头模式
    ch_options.add_argument('--headless')
    # 启动浏览器时加入配置
    driver = webdriver.Chrome(options=ch_options)
    driver.get("https://passporttest.senguo.me")
    # 显式等待加载完成
    WebDriverWait(driver,10,0.2).until(lambda x: x.find_element_by_css_selector("span.item.login-by-phone")).click()
    elem_username = driver.find_element_by_css_selector("input.el-input__inner")
    elem_username.send_keys(phone)
    elem_kwd = driver.find_element_by_css_selector("input.el-input__inner[type~='password']")
    elem_kwd.send_keys(pwd)
    elem_kwd.send_keys(Keys.ENTER)
    # 等待接口响应时间
    time.sleep(3)
    # 取出cookie
    c = driver.get_cookies()
    # 拼接cookie
    cookie = ';'.join([i['name'] +'='+ i['value'] for i in c])
    print(cookie)
    driver.close()
'''
def get_cookie(phone,pwd):
    sha256 = hashlib.sha256()
    sha256.update(pwd.encode('utf-8'))
    dic = {}
    dic['phone'] = phone
    dic['password'] = sha256.hexdigest()
    r = requests.post('http://passporttest.senguo.me/api/login?method=login_by_phone_password'\
        ,data=dic)
    try:
        cookies = r.cookies.items()
        cookie = ''
        for name,value in cookies:
            cookie += '{0}={1}'.format(name,value)
        return cookie
    except Exception as err:
        print('获取cookie失败：\n{0}'.format(err))


