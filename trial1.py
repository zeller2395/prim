StudyLengthDay= 30
StudyLengthEnd= 60
StudyLengthRequired= 150
print("When I study on a weekday, it is for " + str(StudyLengthDay) + " minutes a day.")
print("When I study on a weekend day, it is for " + str(StudyLengthEnd) + " minutes a day.")
print("I need to study at least " + str(StudyLengthRequired) + " minutes for the week.")

WeekdaysStudied= int(input("How many weekdays did you study for this week?: "))
WeekendDaysStudied= int(input("How many weekend days did you study for this week?: "))


TotalWeekdayMinutesStudied= (WeekdaysStudied * StudyLengthDay)
TotalWeekendMinutesStudied= (WeekendDaysStudied * StudyLengthEnd)
TotalWeekMinutesStudied= (TotalWeekdayMinutesStudied + TotalWeekendMinutesStudied)
MinutesNeeded= StudyLengthRequired-TotalWeekMinutesStudied

print("You studied for " + str(TotalWeekMinutesStudied) + " minutes this week.")
if TotalWeekMinutesStudied>= StudyLengthRequired:
    print("Congrats, you have studied for the appropriate amount of time.")
elif TotalWeekMinutesStudied>= 90:
    print("You came up " + str(MinutesNeeded) + " minutes short of your goal.")
    print("Close, but no cigar. Keep studying.")
elif TotalWeekMinutesStudied< 90:
    print("You came up " + str(MinutesNeeded) + " minutes short of your goal.")
    print("This is pathetic. Study more next week.")
