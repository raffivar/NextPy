def gen_hrs():
    for i in range(0, 24):
        yield i


def gen_mins():
    for i in range(0, 60):
        yield i


def gen_secs():
    for i in range(0, 60):
        yield i


def gen_time():
    for h in gen_hrs():
        for m in gen_mins():
            for s in gen_secs():
                yield "%02d:%02d:%02d" % (h, m, s)


def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    for i in range(1, 13):
        yield i


def gen_days(month, leap_year=True):
    stop = 0
    if month == 2:
        if leap_year:
            stop = 30
        else:
            stop = 29
    elif month in (1, 3, 5, 7, 8, 10, 12):
        stop = 32
    elif month in (4, 6, 9, 11):
        stop = 31

    for i in range(1, stop):
        yield i


def gen_date():
    for y in gen_years(2020):
        for m in gen_months():
            for d in gen_days(m, is_leap_year(y)):
                yield "%02d/%02d/%0004d" % (d, m, y)


def main():
    gd = gen_date()

    for i in range(5):
        date = next(gd)
        for gt in gen_time():
            print("{} {}".format(date, gt))

    # for i in range(700):
    #     print(next(gd))


if __name__ == "__main__":
    main()
