from datetime import datetime
import time

def convert_to_unix(date_str):
    date_time_obj = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
    unixtime = int(time.mktime(date_time_obj.timetuple()))

    return unixtime

def convert_from_unix(unix_date):
    ret_date = datetime.utcfromtimestamp(unix_date)

    return ret_date