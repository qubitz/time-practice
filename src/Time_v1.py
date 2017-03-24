inputNotReceived = True

while inputNotReceived:
    try:
        # Get starting time from user (hours, minutes)
        enteredTime = input("Enter starting time (HH:MM): ").strip().split(':')
        startHour, startMinute = map(int, enteredTime) # may throw ValueError

        if (1 >= startHour or startHour >= 12) and (0 > startMinute or startMinute >= 60):
            print("Entered time not valid")
        else:
            inputNotReceived = False # successful input

    except ValueError:
        print("Must enter a time (ex: 5:09)")

inputNotReceived = True

while inputNotReceived:
    try:
        # Get timer value from user (hours)
        enteredTimerHour = input("Enter timer value: ")
        timerHour = int(enteredTimerHour)

        if timerHour < 0:
            print("Entered value not valid")
        else:
            inputNotReceived = False
    except ValueError:
        print("Must enter a number")

sumHours = startHour + timerHour
if 0 > sumHours or sumHours > 12:
    endHour = sumHours % 12
else:
    endHour = sumHours

endTime = "{0}:{1:02d}".format(endHour, startMinute)
print(endTime)
