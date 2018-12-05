#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.BasePage import PageConstructor


class ActionForm(PageConstructor):
    # locators for this page
    FIRST_NAME_INPUT = (By.ID, 'firstname')
    LAST_NAME_INPUT = (By.ID, 'lastname')
    GO_BUTTON = (By.NAME, 'form')

    def exploit(self, firstname, lastname):
        first_input = self.findElement(self.FIRST_NAME_INPUT)
        first_input.send_keys(firstname)
        last_input = self.findElement(self.LAST_NAME_INPUT)
        last_input.send_keys(lastname)
        self.findVisibleElement(self.GO_BUTTON).click()
