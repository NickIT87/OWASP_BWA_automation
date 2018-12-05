#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.BasePage import PageConstructor
from selenium.webdriver.support.ui import Select


class BugListForm(PageConstructor):
    # locators for this page
    DROPDOWN_BUG_LIST = (By.XPATH, '//*[@id="bug"]/form/select')
    HACK_BUTTON = (By.NAME, 'form_bug')

    def chose_feature(self, value):
        select = Select(self.findElement(self.DROPDOWN_BUG_LIST))
        select.select_by_value(value)
        hack = self.findElement(self.HACK_BUTTON)
        hack.click()
