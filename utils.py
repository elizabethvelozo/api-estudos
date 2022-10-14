from datetime import datetime

def convert_timestamp(timestamp):
    return datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

def elapsed_minutes(timestamp):
    elapsed_time = datetime.now() - convert_timestamp(timestamp)
    elapsed_minutes = elapsed_time.seconds / 60

    return elapsed_minutes