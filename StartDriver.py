from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class StartDriver:

    @staticmethod
    def webDrvierRun(path):
        driver = webdriver.Firefox(executable_path=path)
        assert Options.headless  # Без графического интерфейса
        driver.maximize_window()
        return driver
