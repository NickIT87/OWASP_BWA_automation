#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *
from pages.MainPage import BugListForm


#____________ Global step - login to resource _________
@Given('select option {value} in the bug list and press hack')
def step_select_feature_to_test(context, value):
    BugListForm(context.driver).chose_value(value)



    #context.driver.maximize_window()
    #context.driver.get(LoginForm.URL)
    #LoginForm(context.driver).login()
    #auth_form = LoginForm(context.driver)
    #auth_form.login()

@Then('enter data {firstname}, {lastname} and submit the form')
def step_filling_the_form(context, firstname, lastname):
    pass