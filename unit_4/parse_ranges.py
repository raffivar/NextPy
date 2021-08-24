def parse_ranges(ranges):
    ranges_str_gen = (rng.split('-') for rng in ranges.split(','))
    ranges_rng_gen = (range(int(start), int(stop) + 1) for start, stop in ranges_str_gen)
    num_gen = (num for rng in ranges_rng_gen for num in rng)

    lst = []
    for num in num_gen:
        lst.append(num)
    return lst


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == "__main__":
    main()
