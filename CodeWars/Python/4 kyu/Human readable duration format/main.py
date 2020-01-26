def s_or_empty(num):
    return 's' if num > 1 else ''
    
def format_duration(s):
    if not s: return 'now'
    years = s//31536000
    days = (s - years * 31536000)//86400
    hours = (s - (years * 31536000 + days * 86400))//3600
    minutes = (s - (years * 31536000 + days * 86400 + hours * 3600))//60
    seconds = s % 60
    res = ''
    if years and days and hours and minutes and seconds:
        return '{} year{}, {} day{}, {} hour{}, {} minute{} and {} second{}'.format(years, s_or_empty(years), 
                                                                                    days, s_or_empty(days),
                                                                                    hours, s_or_empty(hours),
                                                                                    minutes, s_or_empty(minutes),
                                                                                    seconds, s_or_empty(seconds))
    elif days and hours and minutes and seconds:
        return '{} day{}, {} hour{}, {} minute{} and {} second{}'.format(days, s_or_empty(days),
                                                                         hours, s_or_empty(hours),
                                                                         minutes, s_or_empty(minutes),
                                                                         seconds, s_or_empty(seconds))
    elif hours and minutes and seconds:
        return '{} hour{}, {} minute{} and {} second{}'.format(hours, s_or_empty(hours),
                                                               minutes, s_or_empty(minutes),
                                                               seconds, s_or_empty(seconds))
    elif minutes and seconds:
        return '{} minute{} and {} second{}'.format(minutes, s_or_empty(minutes),
                                                    seconds, s_or_empty(seconds))
    elif years and days and hours and minutes:
        return '{} year{}, {} day{}, {} hour{} and {} minute{}'.format(years, s_or_empty(years),
                                                                       days, s_or_empty(days),
                                                                       hours, s_or_empty(hours),
                                                                       minutes, s_or_empty(minutes))
    elif seconds:
        return '{} second{}'.format(seconds, s_or_empty(seconds))
    elif minutes:
        return '{} minute{}'.format(minutes, s_or_empty(minutes))
    elif hours:
        return '{} hour{}'.format(hours, s_or_empty(hours))
    