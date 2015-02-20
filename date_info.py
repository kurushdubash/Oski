from datetime import datetime
import requests
time_api = 'GN1SRFT4KGVF'

def get_date():
    date_info = str(datetime.now().date().isoformat())
    stringer = "today is the {0} of {1} in {2}".format(date_info[8:9], date_info[5:6], date_info[0:4])
    return stringer  # YYYY-MM-DD

def get_time_obj():
    try:
        
        time_url = 'http://api.timezonedb.com/?zone=America/Los_Angeles&format=json&key=' + time_api;
        time_data = requests.get(time_url)
        time_data = time_data.json()
        unix_time = time_data['timestamp'] # Gets the time in a unix format, must convert
        datestr = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S') # Converting to a datetime obj
        dateobj = datetime.strptime(datestr,'%Y-%m-%d %H:%M:%S')
        return dateobj
        
    except:
        print("Error getting time.")

def get_minutes(dateobj):
    mins = dateobj.time().__str__() #Gets time in string format of '14:14:18' | %H:%M:%S'
    mins = mins[3:5]
    return int(mins)

def get_hours(dateobj):
    hours = dateobj.time().__str__() #Gets time in string format of '14:14:18' | %H:%M:%S'
    hours = hours[:2]
    return int(hours)

def get_time(dateobj):
    hours = get_hours(dateobj)
    mins = get_minutes(dateobj)
    if hours > 12:
        hours -= 12
    time = str(hours) + ':' + str(mins)
    return time