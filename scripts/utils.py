from datetime import datetime

# Get the current date iand time in ISO 8601 format
def get_timestamp():
    '''Returns the current timestamp in ISO 8601 format with seconds precision.'''
    from datetime import datetime
    return datetime.now().isoformat(timespec='seconds')





