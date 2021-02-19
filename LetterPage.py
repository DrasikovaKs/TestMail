class LetterPage:

    def click_write_to_whom(self):
        self.find_element_by_class_name('composeYabbles').click()

    def fill_write_to_whom(self, mail):
        self.find_element_by_class_name('composeYabbles').send_keys(mail)

    def click(self):
        self.find_element_by_css_selector("div[role='presentation'] > div[role='textbox']").click()

    def click_topic(self):
        self.find_element_by_css_selector('.ComposeSubject-TextField').click()

    def fill_topic(self):
        self.find_element_by_css_selector('.ComposeSubject-TextField').send_keys('Тест')

    def click_text_field(self):
        self.find_element_by_css_selector("div[role='presentation'] > div[role='textbox']").click()

    def fill_text_field(self, text):
        self.find_element_by_css_selector("div[role='presentation'] > div[role='textbox']").send_keys(text)

    def click_send_button(self):
        self.find_element_by_css_selector('.ComposeControlPanelButton-Button_action').click()
