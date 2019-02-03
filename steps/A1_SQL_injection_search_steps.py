#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from behave import *
from pages.elements.A1_SQL_injection_search import searchPOSTmain


#_____ Step 1 - A1 injection: SQL injection (POST/search)_____
@Then('enter data {sql_injection_case} and submit the form')
def step_filling_the_form(context, sql_injection_case):
    searchPOSTmain(context.driver).exploit(sql_injection_case)
    #time.sleep(2)

#_____ Step 2 - A1 injection: SQL injection (POST/search) _____
@When('the form is submited this {err_msg} must be including into table#table_yellow')
def step_check_expected_result(context, err_msg):
    #ActionForm.get_screenshot()
    searchPOSTmain(context.driver).check_actual_result(err_msg)
    #time.sleep(2)