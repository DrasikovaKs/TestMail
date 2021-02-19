import time


class MailPage:

    def check_mail_page(self):
        selector = '.count-me.yandex-header__logo-service.yandex-header__logo-service_lang_ru'
        self.find_element_by_css_selector(selector)
        assert "Почта" in self.title

    def click_write_button(self):
        self.find_element_by_css_selector(".mail-ComposeButton-Text").click()
        time.sleep(3)
