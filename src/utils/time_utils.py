def time_to_minutes(time: str):
    '''Converts time format to minutes'''
    
    number = time[:-1]

    if time.endswith('h'):
        return int(number) * 60
        
    elif time.endswith('m'):
        return int(number)

    else:
        raise ValueError("Cannot convert")

def time_to_minutes_after_midnight(time_str: str):
    '''Converts HH:mm format to minutes after midnight'''

    hours, minutes = map(int, time_str.split(':'))

    return hours * 60 + minutes

def minutes_after_midnight_to_time(minutes: int):
    '''Converts minutes after midnight to HH:mm format'''

    hours = int(minutes / 60)
    
    minutes = minutes % 60
    
    return "{:02d}:{:02d}".format(hours, int(minutes))