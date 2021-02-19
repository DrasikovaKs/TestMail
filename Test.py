from LoginPage import LoginPage
from MailPage import MailPage
from LetterPage import LetterPage
from StartDriver import StartDriver
from config import *

driver = StartDriver.webDrvierRun(GECKODRIVERPATH)
driver.get("https://www.tut.by/")

LoginPage.click_enter(driver)
LoginPage.fill_field_login(driver, LOGIN)
LoginPage.fill_field_password(driver, PASSWORD)
LoginPage.click_mark(driver)
LoginPage.click_button_enter(driver)
LoginPage.click_mail_button(driver)

MailPage.check_mail_page(driver)
MailPage.click_write_button(driver)

LetterPage.click_write_to_whom(driver)
LetterPage.fill_write_to_whom(driver, MAIL)

LetterPage.click(driver)
LetterPage.click_topic(driver)
LetterPage.fill_topic(driver)
LetterPage.click_text_field(driver)
LetterPage.fill_text_field(driver, TEXT)
LetterPage.click_send_button(driver)
driver.close()
quit()

