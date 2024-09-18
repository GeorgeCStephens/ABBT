from datetime import date
from datetime import timedelta

def ask():

    #Generate dates for up to a week
    allFutureDates=[]
    baseDate = date.today()
    for i in range(7):
        allFutureDates.append(baseDate + timedelta(days=i))

    #Print out all dates
    allDatesInt=len(allFutureDates)+1
    print("Dates To Choose From")
    for i in range(len(allFutureDates)):
        print(" " + str(i) + ": " + str(allFutureDates[i]))
    print(" " + str(allDatesInt) + ": All future dates")
    
    #Ask for the users input
    print("")
    dateChosen=int(input("Desired Date: "))

    #Return back the desired date
    if dateChosen == allDatesInt:
        return allFutureDates
    else:
        return allFutureDates[dateChosen]   