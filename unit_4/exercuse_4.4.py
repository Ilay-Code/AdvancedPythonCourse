import datetime


def gen_seconds():
    for sec in range(60):
        yield sec


def gen_minutes():
    for min in range(60):
        yield min


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for min in gen_minutes():
            for sec in gen_seconds():
                yield "%02d:%02d:%02d" % (hour, min, sec)


def gen_years(start=2019):
    current_year = datetime.datetime.now().year
    year = start

    while True:
        yield year
        year += 1
        if year > current_year:
            current_year = datetime.datetime.now().year


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    yield days_in_month[month]


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def gen_date():
    for year in gen_years():
        leap_year = is_leap_year(year)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


def main():
    date_gen = gen_date()
    for i in range(1, 10000001):
        date = next(date_gen)
        if i % 1000000 == 0:
            print(date)


if __name__ == '__main__':
    main()
