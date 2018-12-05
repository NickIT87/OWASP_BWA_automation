#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from behave import *
from pages.MainPage import BugListForm
from pages.elements.A1_HTML_reflectedGET import ActionForm


#____________ Global step - select feature to test _________
@Given('select option {value} in the bug list and press hack')
def step_select_feature_to_test(context, value):
    BugListForm(context.driver).chose_feature(value)

#________ Step - test HTML injection reflected(GET) ________
@Then('enter data {firstname}, {lastname} and submit the form')
def step_filling_the_form(context, firstname, lastname):
    ActionForm(context.driver).exploit(firstname, lastname)

#____Step - expected result: injection code not included____
#_______ "<div id=main>" include <firstname> string ________
@When('the form is submited this {firstname} string must be including into div#main')
def step_check_expected_result(context, firstname):
    ActionForm(context.driver).check_actual_result(firstname)
    #time.sleep(2)