#!/usr/bin/env python3

import interactWithSite
import inputDates

desiredDate=inputDates.ask()

if type(desiredDate) == list:
    allAvailableSlots=[]
    print("GETTING ALL DATES AVAILABLE")
    print("---THIS MAY TAKE A WHILE---")
    for date in desiredDate:
        driver, futureSlots=interactWithSite.getAllAvailableSlots(date)
        allAvailableSlots.append(futureSlots)
    print("===========================")
    for day in range(len(allAvailableSlots)):
        print("")
        print(desiredDate[day])
        print("----------")
        for slot in allAvailableSlots[day]:
            print(slot["court"]+" is free at "+slot["time"])
else:
    driver, allAvailableSlots=interactWithSite.getAllAvailableSlots(desiredDate)
    print("--------------")
    for slot in allAvailableSlots:
        print(slot["court"]+" is free at "+slot["time"])