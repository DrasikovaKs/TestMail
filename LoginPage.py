import time


class LoginPage:

    def click_enter(self):
        self.find_element_by_link_text('Войти').click()

    def fill_field_login(self, login):
        self.find_element_by_name('login').send_keys(login)

    def fill_field_password(self, password):
        self.find_element_by_name('password').send_keys(password)

    def click_mark(self):
        self.find_element_by_id('memory').click()

    def click_button_enter(self):
        self.find_element_by_css_selector("input[value='Войти']").click()

    def click_mail_button(self):
        self.find_element_by_link_text('Почта').click()
        time.sleep(3)