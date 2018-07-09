import datetime as dt

m, d = map(int, input().split(' '))

date = dt.date(2007, m, d)

#datetime.weekday() (월요일=0 ~ 일요일=6)
#datetime.isoweekday() (월요일=1 ~ 일요일=7)


def get_day_of_week(input):
    day = {
        0: "MON",
        1: "TUE",
        2: "WED",
        3: "THU",
        4: "FRI",
        5: "SAT",
        6: "SUN"
    }

    return day.get(input)


print(get_day_of_week(date.weekday()))