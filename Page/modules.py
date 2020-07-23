from selenium import webdriver

def login_by_phone(phone,pwd):
    driver = webdriver.Chrome()     #打开谷歌浏览器
    phone = ''
    pwd = ''
    driver.get("url")
    driver.maximize_window()
    #隐式等待页面加载完成后开始对元素操作
    WebDriverWait(driver,10,0.2).until(lambda x: x.find_element_by_css_selector("span.item.login-by-phone")).click()
    # elem_login_by_phone = driver.find_element_by_css_selector("span.item.login-by-phone")
    # driver.find_element_by_css_selector("span.item.login-by-phone").click()
    elem_username = driver.find_element_by_css_selector("input.el-input__inner")
    elem_username.send_keys(phone)
    elem_kwd = driver.find_element_by_css_selector("input.el-input__inner[type~='password']")
    elem_kwd.send_keys(pwd)
    elem_kwd.send_keys(Keys.ENTER)