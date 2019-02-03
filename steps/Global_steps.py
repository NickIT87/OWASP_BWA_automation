#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from behave import *
from pages.MainPage import BugListForm


#___________ Global 0 step - select feature to test ____________
@Given('option {value} in the bug list and press hack')
def step_select_feature_to_test(context, value):
    BugListForm(context.driver).chose_feature(value)