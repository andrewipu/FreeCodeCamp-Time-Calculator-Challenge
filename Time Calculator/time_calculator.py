#------------------------------
#add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

#add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

#add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

#add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

#add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

#add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)


import re

#start = ("2:59 AM", "24:00", "Monday") #Fails  completely ->from Unit Tests.
#start = ("8:16 PM", "466:02", "Monday") #Fails completely ->from Unit Tests.
#start = ("5:01 AM", "0:00", "Monday") #Fails Completely ->from Unit Tests.
#start = ("2:59 AM", "24:00", "saturDay") #Fails Completely ->from Unit Tests.
#start = ("11:59 PM", "24:05", "Wednesday") ##WRONG AM/PM -> Displaying PM instead of AM. ->from Unit Tests.
#start = ("8:16 PM", "466:02", "Tuesday") #Fails Completely ->from Unit Tests. 

start = ("11:59 PM", "24:05", "Wednesday")
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

    index = week_days.index(input_day) #index version of weekdays
    #index = 
    #print("This is index: " + str(index))
    day_count = 0


        #add 12 if it is in PM format
    if AM_PM == 'PM':
            start_hour = int(start_hour) + 12 #I am adding 12(hrs) to convert start_hour to 24hr clock system.
            new_hour = int(start_hour) + int(dur_hours)

########################################################### -> returns start_hour and new_hour in 24hrs

            days_hours = divmod(new_hour, 24)
            #print(days_hours)

            new_hour = days_hours[1] #Assuming this is in 24hrs.

            day_count = day_count + days_hours[0]

            if day_count == 0:
                new_day = input_day

            #A count variable to reference the day_count
            # Once the count variable and day_count variable are equal, end loop.
            # Grab current list position hence grab the day 
            # Each time the index iterates to an new day, increment the count variable.

            count_var = 0
            #i = input_day
            i = index


            while count_var <= day_count:
                for i in range(index, len(week_days)):
                    if count_var > day_count:
                        break
                    count_var += 1
                    new_day = week_days[i]
                    #print(new_day)
                
                #print(new_day)
                    if i >= max(range(len(week_days))):
                        i = week_days.index('Monday')
                        index = i 
                    #new_day = week_days[i]
                    #print(new_day)


            #while count_var < day_count:

                #for i in weekdays
                #for i in range(index, len(week_days)):
                    #count_var += 1
                    #new_day = week_days[i]
                    #print(new_day)
                    #if i >= max(range(len(week_days))):
                       # i = week_days.index('Monday')
                        #new_day = week_days[i]
                        #print(new_day)



######################################################## -> returns the current day, and hour.
            #new minutes
            new_min = int(start_min) + int(dur_minutes)
            if new_min >=60: #Should this be 59 instead? Because at 60, is when we increment an hour/minute/second.
                new_hour = new_hour + 1
                new_min = new_min - 60
                if new_hour >= 24:
                    #new_day = week_days[i + 1]
                    new_day = week_days[i]
######################################################## -> returns new minutes

    if AM_PM == 'AM':
        new_hour = int(start_hour) + int(dur_hours)
        new_min = int(start_min) + int(dur_minutes)
         
        if new_min >=60:
            new_hour = new_hour + 1
            #print(new_hour)
            new_min = new_min - 60
                
        #get the day
        if new_hour >= 12:
            new_hour = new_hour
        else:
            new_hour = new_hour + 12 #convert the new hour to 24hrs to calculate the date
            days_hours = divmod(new_hour, 24)
            day_count = day_count + days_hours[0]

            i = index
            j = i + day_count
            #print(j)
            if i <= j:
                i = j
                if i >= j:
                    i = i - len(week_days)
            new_day = week_days[i]

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
        if new_hour <= 23 :
            period = 'PM'

    if new_hour >= 24 :
        period = 'AM'


    #check if time is in 24hrs and convert to 12hrs
    if new_hour > 12:
        new_hour=new_hour-12

    elif new_hour <=12:
        new_hour=new_hour

    
    new_hour = str(new_hour)
 
    #print new time in hh : mm format.
    new_time = new_hour + ":" + new_min + " " + period + ", " + new_day
    print(new_time)


add_time()

#redundant operations:
    #- incrementing hour when minutes > 60
    #- the condition that allows me to go beyond the end of list.
    #- method used to grab day and hours