from datetime import date
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from alive_progress import alive_bar
import time


def getAllAvailableSlots(desiredDate):
    print("----------")
    print(desiredDate)

    #Defaults
    enddate = desiredDate + timedelta(days=1)
    url="https://chesterfieldleisure.gladstonego.cloud/book/calendar/QACTSPH001?activityDate="+str(desiredDate)+"T06:00:00.000Z&previousActivityDate="+str(enddate)+"T06:00:00.000Z"


    #Open The Webbrowser
    print("Establishing a connection with the site")
    options = Options()
    options.add_argument("--headless")
    with alive_bar(3) as bar:
        bar()
        driver = webdriver.Firefox(options=options)
        bar()
        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/main/app-language/ng-component/div/div[1]/section/ng-component/div/form/app-activity-calendar-timetable/div/app-overflow-carousel/div/div/div/app-overflow-carousel-slide[1]/div/div/ol/li[1]/app-activity-calendar-timetable-slot/div/h3")))
            bar()
        except:
            print("An error occured whilst connecting to the site!")
            driver.quit()


    #Generate the possible open slots
    print("Scrape all open slots")
    allPossibleSlots=[]
    with alive_bar(100) as bar:
        for i in range(10):
            for j in range(10):
                allPossibleSlots.append("/html/body/app-root/div/main/app-language/ng-component/div/div[1]/section/ng-component/div/form/app-activity-calendar-timetable/div/app-overflow-carousel/div/div/div/app-overflow-carousel-slide["+str(i)+"]/div/div/ol/li["+str(j)+"]/app-activity-calendar-timetable-slot/div/app-button/button/span/span")
                bar()

    #Check all XPaths and store the ones we want
    print("Scrape all possible slots and store matches")
    allBookableSlots=[]
    allBookableSlotsXPath=[]
    with alive_bar(100) as bar:
        for xPath in allPossibleSlots:
            bar()
            try:
                validSlot=driver.find_element(By.XPATH, xPath)
                allBookableSlots.append(validSlot)
                allBookableSlotsXPath.append(xPath)
            except:
                pass

    #Get the time of each slot
    print("Scrape the time and court for all stored matches")
    allTimeSlots=[]
    with alive_bar(len(allBookableSlotsXPath)) as bar:
        for openSlotXPath in allBookableSlotsXPath:
            bar()
            timeXPath=str(openSlotXPath).removesuffix("app-button/button/span/span")+"p"
            timeSlot=driver.find_element(By.XPATH, timeXPath)
            courtXPath=str(openSlotXPath).removesuffix("app-button/button/span/span")+"h3"
            courtSlot=driver.find_element(By.XPATH, courtXPath)
            allTimeSlots.append({"time":timeSlot.text, "court":courtSlot.text,"xPathToBook":str(openSlotXPath)})
        
    #Return our constructed data
    print("All open slots gathered.")
    return driver, allTimeSlots
