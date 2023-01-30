import re

#start = ("2:59 AM", "24:00", "Monday") #PASS
#start = ("8:16 PM", "466:02", "Monday") #PASS
#start = ("5:01 AM", "0:00", "Monday") #PASS
#start = ("2:59 AM", "24:00", "saturDay") #PASS
#start = ("11:59 PM", "24:05", "Wednesday") #PASS
#start = ("8:16 PM", "466:02", "Tuesday") #PASS

#start = ("8:16 PM", "466:02")

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#def add_time():
def add_time(start):
    
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

    #Extract the index of the day input by the user
    #input_day = start[2]
    #index = week_days.index(input_day) #index version of weekdays
    try:

        index = next((i for i, day in enumerate(week_days) if day.lower() == start[2].lower()), None)

    except:
        if len(start) < 3:
            index = None

    day_count = 0


        #add 12 if it is in PM format
    if AM_PM == 'PM':
            start_hour = int(start_hour) + 12 #I am adding 12(hrs) to convert start_hour to 24hr clock system.
            new_hour = int(start_hour) + int(dur_hours)

            #calculate the number of days + current hours
            days_hours = divmod(new_hour, 24)

            new_hour = days_hours[1] #Assuming this is in 24hrs.

            
            day_count = day_count + days_hours[0]

            try:
            #Get new day's index on the list
                new_day_index = (day_count + index) % len(week_days)

            except:
                new_day_index = None

            try:
                new_day = week_days[new_day_index]
            except:
                new_day = None


            #new minutes
            new_min = int(start_min) + int(dur_minutes)
            if new_min >=60: #Should this be 59 instead? Because at 60, is when we increment an hour/minute/second.
                new_hour = new_hour + 1
                new_min = new_min - 60
                try:
                    if new_hour >= 24:
                        day_count = day_count + 1
                        new_day_index = new_day_index + 1
                        new_day = week_days[new_day_index]
                except:
                    pass

                    
######################################################## -> if AM

    if AM_PM == 'AM':
        new_hour = int(start_hour) + int(dur_hours)
        new_min = int(start_min) + int(dur_minutes)

        days_hours = divmod(new_hour, 24)
            #print(days_hours)

        new_hour = days_hours[1] #Assuming this is in 24hrs.

        day_count = day_count + days_hours[0]

        try:
            #Get new day's index on the list
            new_day_index = (day_count + index) % len(week_days)

        except:
            new_day_index = None

        try:
            new_day = week_days[new_day_index]
        except:
            new_day = None

        

         
        if new_min >=60:
            new_hour = new_hour + 1
            #print(new_hour)
            new_min = new_min - 60
            
                

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
    
    try:
        #print new time in hh : mm format.
        new_time = new_hour + ":" + new_min + " " + period + ", " + new_day
        #print(new_time)
    except:
        if index == None:
            if day_count == 1:
                days_elapsed = " (next day)"
            elif index == None:
                no_of_days_elapsed = day_count
                days_elapsed = " (" + str(no_of_days_elapsed) + " days later" + ")"
            new_time = new_hour + ":" + new_min + " " + period + days_elapsed
            #print(new_time)
    #except:
        #if index == None:
            #new_time = new_hour + ":" + new_min + " " + period
            #print(new_time)


#add_time()
    return new_time

#Pending:
    #- Allow user to enter mix of big and small characters for the day. -> DONE
    #- Allow user to not include day in the calculation. -> DONE
    #- ADD FEATURE -> display the number of days later. -> use the divmod calculations
    # - FIX UNIT TESTS -> This is because the add_time function takes in two mandatory parameters. I'm gonna need a parameter for the start-time, duration, and day of the week.
    #- EFFICIENCY -> Get rid of repeated code sections. -> I'll see if I can replace them with functions.