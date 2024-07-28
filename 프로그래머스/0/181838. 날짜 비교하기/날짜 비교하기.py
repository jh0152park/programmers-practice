def date2day(date):
    return date[2] + (date[1] * 30) + (date[0] * 12 * 30)

def solution(date1, date2):
    return 1 if date2day(date1) < date2day(date2) else 0