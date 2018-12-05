#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.BasePage import PageConstructor


class ActionForm(PageConstructor):
    # locators for this page
    FIRST_NAME_INPUT = (By.ID, 'firstname')
    LAST_NAME_INPUT = (By.ID, 'lastname')
    GO_BUTTON = (By.NAME, 'form')
    DIV_MAIN = (By.ID, 'main')

    def exploit(self, firstname, lastname):
        self.findElement(self.FIRST_NAME_INPUT).send_keys(firstname)
        self.findElement(self.LAST_NAME_INPUT).send_keys(lastname)
        self.findVisibleElement(self.GO_BUTTON).click()

    def check_actual_result(self, firstname):
        self.checkTextPresentInElem(self.DIV_MAIN, firstname)