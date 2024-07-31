from PIL import Image, ImageDraw, ImageFont
import calendar
from datetime import datetime
from getTideWindows import getMonthTides
import sys
import os

def __createCalendarImage(year, month, events, output_image_path):
    # Create an image with white background
    img_width, img_height = 1600, 1200
    img = Image.new('RGB', (img_width, img_height), 'white')
    draw = ImageDraw.Draw(img)

    # Load a font
    fontTtf = os.path.join(sys._MEIPASS, "OpenSans-Bold.ttf") # sys._MEIPASS used to access font, replace with ./src/OpenSans-Bold.ttf to run w/o exe
    fontMonth = ImageFont.truetype(fontTtf, 60)
    fontDay = ImageFont.truetype(fontTtf, 50)
    fontSmall = ImageFont.truetype(fontTtf, 20)

    # Set up calendar layout
    cal = calendar.monthcalendar(year, month)
    cell_width = img_width // 7
    cell_height = img_height // (len(cal) + 1)  # Extra row for the month name

    # Draw month and year
    # Calculate text size
    text_width = draw.textlength(calendar.month_name[month], font=fontMonth)
    draw.text((800 - text_width, 20), f"{calendar.month_name[month]} {year}", font=fontMonth, fill='black')

    # Draw days of the week
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, day in enumerate(days):
        draw.text((i * cell_width + 20, 120), day, font=fontDay, fill='black')

    # Draw calendar days
    for week_idx, week in enumerate(cal):
        for day_idx, day in enumerate(week):
            if day != 0:
                x = day_idx * cell_width
                y = 200 + week_idx * cell_height
                draw.rectangle([x, y, x + cell_width, y + cell_height], outline='black')
                draw.text((x + 20, y + 20), str(day), font=fontSmall, fill='black')

                # Add time for day
                if day in events:
                    times = events[day]
                    for idx, time in enumerate(times):
                        draw.text((x + 20, y + 60 + idx*40), "Leave By " + str(events[day][idx]), font=fontSmall, fill='black')

    # Save the image
    img.save(output_image_path)

def createCalendar(month, year, save_name):
    # Example usage
    dailyTides = getMonthTides(month, year)
    # Convert into dictionary by day
    dailyTidesDict = {}
    for item in dailyTides:
        # Get date string
        tideDateTimeObj = datetime.strptime(item["t"], "%Y-%m-%d %H:%M")
        tideTimeStr = datetime.strftime(tideDateTimeObj, "%I:%M %p")
        tideDay = int(datetime.strftime(tideDateTimeObj, "%d"))
        if not tideDay in dailyTidesDict:
            dailyTidesDict[tideDay] = []

        # add new element
        dailyTidesDict[tideDay].append(tideTimeStr)

    __createCalendarImage(year, month, dailyTidesDict, save_name)

