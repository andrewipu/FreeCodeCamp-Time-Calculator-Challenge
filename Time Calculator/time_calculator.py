#code works well with "11:59 AM", "2:32"
#code works well with "12:00 PM", "12:00" -> prints: 12:00 AM.
import re
start = ("11:43 PM", "24:20", "Sunday")
#new_hour = ''
#new_hour_test = ''
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def add_time():
    
    #Extract the "Start Hour"
    start_hour = re.findall('\d\S*(?=:)',str (start))[0]

    #Extract "start minutes"
    start_min = re.findall('\d+(?= )',str (start))[0]
    
    #extract AM/PM
    AM_PM = re.findall('\S[PM]',str (start))[0]

    #Extract duration_hours
    #\s\d+(?=:) <- works so far...
    dur_hours = re.findall('\d\S*(?=:)', str (start))[1]

    #Extract dur_minutes
    dur_minutes = re.findall('(?=\d+)\d+', str (start))[3]

    #Extract day -> might need a try/catch in case there isn't a day specified by the user.
    input_day = start[2]
    #print(input_day)

    index = week_days.index(input_day)
    day_count = 0


        #add 12 if it is in PM format
    if AM_PM == 'PM':
            start_hour = int(start_hour) + 12
            new_hour = int(start_hour) + int(dur_hours)
########################################################### -> returns start_hour and new_hour in 24hrs

            days_hours = divmod(new_hour, 24)

            new_hour = days_hours[1]
            #new_day = input_day <- I don't think this is necessary

            day_count = day_count + days_hours[0]
            i = index
            j = i + day_count
            if i <= j:
                i = j
                if i >= j:
                    i = i - len(week_days)
            new_day = week_days[i]
######################################################## -> returns the current day, and hour.
            #new minutes
            new_min = int(start_min) + int(dur_minutes)
            if new_min >=60:
                new_hour = new_hour + 1
                new_min = new_min - 60
######################################################## -> returns new minutes
            if new_hour >= 24:
                #get days and hours
                days_hours = divmod(new_hour, 24) #-> should give a tuple pair
                day_count = day_count + days_hours[0]
                i = index
                j = i + day_count
                if i <= j:
                    i = j
                    if i >= j:
                        i = i - len(week_days)
                new_day = week_days[i]
                new_hour = days_hours[1]
######################################################## -> returns the current day, and hour on condition that new_hour is > 24.
    if AM_PM == 'AM':
        new_hour = int(start_hour) + int(dur_hours)
        new_min = int(start_min) + int(dur_minutes)
        if new_min >=60:
            new_hour = new_hour + 1
            new_min = new_min - 60
######################################################## -> returns the current hour and minutes when set to AM
            
                

    #format as "mm"
    if new_min < 10:
        new_min = "0" + str(new_min)
    else:
        new_min = str(new_min)

    #check and assign the appropriate period (AM or PM)
    if new_hour >= 0 :
        if new_hour < 12:
            period = 'AM'
    if new_hour >= 12 :
        if new_hour <= 24 :
            period = 'PM'


    #check if time is in 24hrs and convert to 12hrs
    if new_hour == 0 :
        new_hour = new_hour + 12
    if new_hour > 12 :
        if new_hour < 24 :
            new_hour = new_hour % 12
    
    new_hour = str(new_hour)
 
    #print new time in hh : mm format.
    new_time = new_hour + ":" + new_min + " " + period + ", " + new_day
    print(new_time)


add_time()

#redundant operations:
    #- incrementing hour when minutes > 60
    #- the condition that allows me to go beyond the end of list.
    #- method used to grab day and hours
    #-