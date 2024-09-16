from datetime import date
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

startdate = date.today()
enddate = startdate + timedelta(days=1)
url="https://chesterfieldleisure.gladstonego.cloud/book/calendar/QACTSPH001?activityDate="+str(startdate)+"T06:00:00.000Z&previousActivityDate="+str(enddate)+"T06:00:00.000Z"


#Open The Webbrowser
print("Open up the webbrowser...")
driver=webdriver.Firefox()
driver.get(url)
time.sleep(7)
print("     Done")

#Generate the possible open slots
print("Generating Button XPaths...")
allPossibleSlots=[]
for i in range(10):
    for j in range(10):
        allPossibleSlots.append("/html/body/app-root/div/main/app-language/ng-component/div/div[1]/section/ng-component/div/form/app-activity-calendar-timetable/div/app-overflow-carousel/div/div/div/app-overflow-carousel-slide["+str(i)+"]/div/div/ol/li["+str(j)+"]/app-activity-calendar-timetable-slot/div/app-button/button/span/span")
print("     Done")

#Check all XPaths and store the ones we want
print("Building List Of Open Slots...")
allAvailableSlots=[]
allAvailableSlotsXPath=[]
for xPath in allPossibleSlots:
    try:
        validSlot=driver.find_element(By.XPATH, xPath)
        allAvailableSlots.append(validSlot)
        allAvailableSlotsXPath.append(xPath)
    except:
        pass
print("     Done")

#Get the time of each slot
print("Gathering Times Of Available Slots...")
for openSlotXPath in allAvailableSlotsXPath:
    timeXPath=str(openSlotXPath).removesuffix("app-button/button/span/span")+"p"
    timeSlot=driver.find_element(By.XPATH, timeXPath)
    print(timeSlot)
print("     Done")

#allOpenSlots=driver.find_elements(By.XPATH, "//*[contains(text(), 'Book now')]")

#/html/body/app-root/div/main/app-language/ng-component/div/div[1]/section/ng-component/div/form/app-activity-calendar-timetable/div/app-overflow-carousel/div/div/div/app-overflow-carousel-slide[1]/div/div/ol/li[2]/app-activity-calendar-timetable-slot/div/div
#/html/body/app-root/div/main/app-language/ng-component/div/div[1]/section/ng-component/div/form/app-activity-calendar-timetable/div/app-overflow-carousel/div/div/div/app-overflow-carousel-slide[1]/div/div/ol/li[3]/app-activity-calendar-timetable-slot/div/app-button/button/span/span