from selenium import webdriver
from pages.LoginPage import LoginForm

def before_feature(context, scenario):
    # for local driver
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)

def before_scenario(context, scenario):
    context.driver.maximize_window()
    context.driver.get(LoginForm.URL)
    LoginForm(context.driver).login()

def after_feature(context, scenario):
    context.driver.quit()