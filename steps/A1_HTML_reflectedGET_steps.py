#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from behave import *
from pages.elements.A1_HTML_reflectedGET import ActionForm


#_____ Step 1 - A1 injection: HTML injection reflected(GET)_____
@Then('enter data {firstname}, {lastname} and submit the form')
def step_filling_the_form(context, firstname, lastname):
    ActionForm(context.driver).exploit(firstname, lastname)

#_____ Step 2 - A1 injection: HTML injection reflected(GET)_____
@When('the form is submited this {firstname} string must be including into div#main')
def step_check_expected_result(context, firstname):
    #ActionForm.get_screenshot()
    ActionForm(context.driver).check_actual_result(firstname)
    #time.sleep(2)