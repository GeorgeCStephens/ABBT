from datetime import date
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

startdate = date.today()
enddate = startdate + timedelta(days=1)
url="https://chesterfieldleisure.gladstonego.cloud/book/calendar/QACTSPH001?activityDate="+str(startdate)+"T06:00:00.000Z&previousActivityDate="+str(enddate)+"T06:00:00.000Z"

driver=webdriver.Firefox()
driver.get(url)
time.sleep(5)