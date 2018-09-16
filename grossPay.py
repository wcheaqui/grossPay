# Calculate gross pay
def pay(regHours, rate):
    try:
        grossPay = round((regHours * rate), 2)
        return grossPay
    except:
        return 'please check your answer'


# Modifies hours to meet minimum pay
def minimum(hours):
    if hours < 8:
        return 8
    else:
        return hours

# Converts Hours and Minutes into Hours
def hoursConversion(day):
    hours = input('Regular hours worked ' + day + '?\n')
    minutes = input('Regular minutes worked ' + day + '?\n')
    otHours = input('OT hours worked ' + day + '?\n')
    otMinutes = input('OT minutes worked ' + day + '?\n')
    makeupTime = input('Makeup minutes ' + day + '?\n')
    return float(int(hours) + int(minutes) / 60) + ((int(otHours) + int(otMinutes) / 60) - int(makeupTime) / 60) * 1.5


# Hours for Daly Input
day1 = hoursConversion('day 1')
day2 = hoursConversion('day 2')
day3 = hoursConversion('day 3')
day4 = hoursConversion('day 4')
day5 = hoursConversion('day 5')
day6 = hoursConversion('day 6')
day7 = hoursConversion('day 7')
day8 = hoursConversion('day 8')
day9 = hoursConversion('day 9')
day10 = hoursConversion('day 10')

# Calculates Total Number of Hours
hoursOfPay = minimum(day1) + minimum(day2) + minimum(day3) + minimum(day4) + minimum(day5) + minimum(day6) + minimum(
    day7) + minimum(day8) + minimum(day9) + minimum(day10)

rateOfPay = 21.58

print('Gross Pay: ' + str(pay(hoursOfPay, rateOfPay)))