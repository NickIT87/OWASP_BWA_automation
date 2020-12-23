from selenium import webdriver
from pages.LoginPage import LoginForm


def before_feature(context, scenario):
    # remote driver
    capabilities = {
        "browserName": "chrome",
        "version": "77.0",
        "enableVNC": False,
        "enableVideo": True
    }
    context.driver = webdriver.Remote(
        command_executor="http://192.168.0.103:4444/wd/hub",
        desired_capabilities=capabilities
    )

    # for local driver
    # context.driver = webdriver.Chrome()
    # context.driver.implicitly_wait(10)

def before_scenario(context, scenario):
    context.driver.maximize_window()
    context.driver.get(LoginForm.URL)
    LoginForm(context.driver).setSecurityLevel("high")
    LoginForm(context.driver).login()

def after_feature(context, scenario):
    #context.driver.close()
    pass