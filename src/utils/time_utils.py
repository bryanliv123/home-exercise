from datetime import datetime, timedelta


def time_to_minutes(time: str):
    '''Converts time format to minutes'''
    
    if not time:
        raise ValueError("Cannot convert")

    number = time[:-1]

    if time.endswith('h'):
        return int(number) * 60
        
    elif time.endswith('m'):
        return int(number)

    else:
        raise ValueError("Cannot convert")

def subtract_minutes_from_time(minutes: float, time: str, format = '%H:%M'):
    diff = datetime.strptime(time, format) - timedelta(minutes=minutes)

    return diff.time().strftime(format)
