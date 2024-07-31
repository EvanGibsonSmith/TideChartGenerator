import requests
from datetime import datetime, timedelta
import json

def getLowTides(tideData):
    lowTides = []
    windowSize = 4
    index = windowSize//2
    while index<len(tideData)-windowSize//2: # loop through index until end of tide window
        point = tideData[index]
        windowValues = [float(value["v"]) for value in tideData[index-windowSize//2:index+windowSize//2+1]]
        if (float(point["v"])==min(windowValues)):
            lowTides.append(point) # after low tide found, "skip ahead an hour" since this one found
            index += 6

        index+=1

    return lowTides

def checkWithinDay(elem, earlyTime=6, endTime=21):
    hour = datetime.strptime(elem["t"], "%Y-%m-%d %H:%M").hour
    return (hour>earlyTime) and (hour<endTime)

def incMonth(month):
    if (month==11):
        return 1
    return month+1

def getMonthTides(month, year):
    # Tide link
    month_start = datetime(year=datetime.today().year, month=month, day=1) # Gets this month, no matter the day in the month
    beginDate = datetime.strftime(month_start, "%Y%m%d")
    endDate = datetime.strftime(datetime(year=year, month=incMonth(month), day=1) - timedelta(days=1), "%Y%m%d") # Get last day of month (get next month, subtract one day)
    barHarborTides = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date="+beginDate+"&end_date="+endDate+\
        "&station=8413320&product=predictions&datum=MLLW&time_zone=lst_ldt&units=english&application=TideWindowPaper&format=json" # Get api call

    tideData = json.loads(requests.get(barHarborTides).text)["predictions"]
    lowTides = getLowTides(list(tideData))
    dayTimeLowTides = list(filter(checkWithinDay, lowTides))
    return dayTimeLowTides