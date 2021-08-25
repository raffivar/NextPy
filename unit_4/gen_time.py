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


def main():
    for gt in gen_time():
        print(gt)


if __name__ == "__main__":
    main()
