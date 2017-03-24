def isValidHour(hour):
    return (1 <= hour and hour <= 12)

def isValidMinute(minute):
    return (0 <= minute < 60)

def isValidTime(hour, minute):
    return (isValidHour(hour) and isValidMinute(minute))

def getStartTime():
    try:
        # Get starting time from user (hours, minutes)
        enteredTime = input("Enter starting time (HH:MM): ").strip().split(':')
        startHour, startMinute = map(int, enteredTime) # may throw ValueError

        if not isValidTime(startHour, startMinute):
            print("Entered time not valid")
            startHour, startMinute = getStartTime()

    except ValueError:
        print("Must enter a time (ex: 5:09)")
        startHour, startMinute = getStartTime()

    return startHour, startMinute

def isValidTimerHour(timerHour):
    return timerHour > 0

def getTimerHour():
     try:
         # Get timer value from user (hours)
         enteredTimerHour = input("Enter timer value: ")
         timerHour = int(enteredTimerHour)

         if not isValidTimerHour:
             print("Entered value not valid")
             timerHour = getTimerHour()

     except ValueError:
         print("Must enter a number")
         timerHour = getTimerHour()

     return timerHour

def calculateEndHour(startHour, timerHour):
    sumHours = startHour + timerHour
    if not isValidHour(sumHours):
        endHour = sumHours % 12
    else:
        endHour = sumHours
    return endHour

def printEndTime(endHour, endMinute):
    endTime = "{0}:{1:02d}".format(endHour, endMinute)
    print(endTime)

startHour, startMinute = getStartTime()
timerHour = getTimerHour()
endHour = calculateEndHour(startHour, timerHour)
printEndTime(endHour, startMinute)
