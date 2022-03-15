from ast import match_case
from calendar import WEDNESDAY


def add_time(start, duration, startDay = ""):

    timeArr = duration.split(":")
    hrDur  = int(timeArr[0])
    mnDur = int(timeArr[1])

    timeArr = start.split(":")
    hrStart = int(timeArr[0])
    mnStart = int(timeArr[1].split()[0])
    period = timeArr[1].split()[1]

    if period == "PM":
        hrStart += 12

    minutes = mnDur+ mnStart
    mnDur = (minutes//60)
    minutes -= mnDur *60
    hour = mnDur
    hour += hrDur + hrStart 
    numDays = (hour//24)
    hour -= numDays*24


    if hour>12:
        period = "PM"
        hour -=12
    elif hour == 12:
        period = "PM"
    elif hour == 0:
        hour = 12
        period = "AM"
    else:
        period = "AM"
    
    new_time = str(hour) + ":" + str(minutes).zfill(2) + " " +  str(period)

    if startDay != "":
        arrWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        startIndex = arrWeek.index(startDay.lower().capitalize())
        endIndex = (startIndex + numDays) % 7
        endDay = arrWeek[endIndex]
        new_time += ", " + endDay

    if numDays == 1:
        new_time += " (next day)"
    elif numDays >1:
        new_time += " (" + str(numDays) +" days later)"

    return new_time

print(add_time("11:55 AM", "3:12"))