#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.BasePage import PageConstructor


class searchPOSTmain(PageConstructor):
    # locators for this page
    FORM_ACTION_INPUT = (By.ID, 'title')
    SEARCH_BUTTON = (By.NAME, 'action')
    TABLE_YELLOW = (By.ID, 'table_yellow')

    def exploit(self, sql_injection_case):
        self.findElement(self.FORM_ACTION_INPUT).send_keys(sql_injection_case)
        self.findVisibleElement(self.SEARCH_BUTTON).click()

    def check_actual_result(self, err_msg):
        #self.get_screenshot()
        self.checkTextPresentInElem(self.TABLE_YELLOW, err_msg)
