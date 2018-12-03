#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *
from pages.LoginPage import LoginForm


#____________ Global step - login to resource _________
@Given('Login to bWAPP as a bee user')
def step_login_as_bee_user(context):
    context.driver.maximize_window()
    context.driver.get(LoginForm.URL)
    LoginForm(context.driver).login()
    #auth_form = LoginForm(context.driver)
    #auth_form.login()

