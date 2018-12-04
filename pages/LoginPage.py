#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.BasePage import PageConstructor


class LoginForm(PageConstructor):
    # locators for this page
    URL = 'http://192.168.0.104/bWAPP/login.php'
    LOGIN_INPUT = (By.NAME, 'login')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'form')

    def login(self, username='bee', password='bug'):
        userlogin_field = self.findElement(self.LOGIN_INPUT)
        userlogin_field.send_keys(username)
        password_field = self.findElement(self.PASSWORD_INPUT)
        password_field.send_keys(password)
        login_btn = self.findVisibleElement(self.LOGIN_BUTTON)
        login_btn.click()
