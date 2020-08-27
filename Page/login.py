from modules import Action
from selenium.webdriver.common.keys import Keys

class Login(Action):
    input_logByphone_loc = ('css_selector','span.item.login-by-phone')
    input_phone_loc = ('css_selector','input.el-input__inner')
    input_password_loc = ('css_selector',"input.el-input__inner[type~='password']")