from config import *
from StartDriver import StartDriver

driver = StartDriver.webDrvierRun(GECKODRIVERPATH)
driver.get("https://www.tut.by/")

driver.close()
quit()
