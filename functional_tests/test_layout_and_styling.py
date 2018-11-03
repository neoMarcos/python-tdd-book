# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Camilla entra na página online
        self.browser.get(self.live_server_url)
        self.browser.maximize_window()

        # Ela percebe que a caixa de entrada está bem centralizada
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            self.browser.get_window_size()['width']/2,
            delta=10
            )

        # Camilla comeca uma nova lista and vê que também está centralizado
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            self.browser.get_window_size()['width']/2,
            delta=10
            )

if __name__ == '__main__':
    unittest.main(warnings='ignore')
