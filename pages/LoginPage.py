#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.BasePage import PageConstructor
from selenium.webdriver.support.ui import Select


class LoginForm(PageConstructor):
    # locators for this page
    URL = 'http://192.168.0.101/bWAPP/login.php'
    LOGIN_INPUT = (By.NAME, 'login')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'form')
    DROPDOWN_SECURITY_LEVEL = (By.NAME, 'security_level')

    def login(self, username='bee', password='bug'):
        userlogin_field = self.findElement(self.LOGIN_INPUT)
        userlogin_field.send_keys(username)
        password_field = self.findElement(self.PASSWORD_INPUT)
        password_field.send_keys(password)
        login_btn = self.findVisibleElement(self.LOGIN_BUTTON)
        login_btn.click()

    def setSecurityLevel(self, value):
        select = Select(self.findElement(self.DROPDOWN_SECURITY_LEVEL))
        select.select_by_visible_text(value)