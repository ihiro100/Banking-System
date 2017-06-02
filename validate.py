__author__ = 'user'
import re

def validate_date(date_from,date_to):
    pattern = "^[0-9]{1,2}-(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)-([0-9]{4})$"
    if re.match(pattern,date_from) and re.match(pattern,date_to):
        date = date_from.split('-')
        if int(date[0]) > 0 and int(date[0]) <= 31 and int(date[2]) > 999:
            date2 = date_to.split('-')
            if int(date2[0]) > 0 and int(date2[0]) <= 31 and int(date2[2]) > 999:
                day_from = int(date[0])
                day_to = int(date2[0])
                mon_from = get_month(date[1])
                mon_to = get_month(date2[1])
                year_from = date[2]
                year_to = date2[2]
                if year_from < year_to:
                    return True
                elif year_from == year_to:
                    if mon_from < mon_to:
                        return True
                    elif mon_from == mon_to:
                        if day_from <= day_to:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

            else:
                return False
        else:
            return False
    else:
        return False

def get_month(month):
    if month == "jan":
        return 1
    elif month == "feb":
        return 2
    elif month == "mar":
        return 3
    elif month == "apr":
        return 4
    elif month == "may":
        return 5
    elif month == "jun":
        return 6
    elif month == "jul":
        return 7
    elif month == "aug":
        return 8
    elif month == "sep":
        return 9
    elif month == "oct":
        return 10
    elif month == "nov":
        return 11
    elif month == "dec":
        return 12
