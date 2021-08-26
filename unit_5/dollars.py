from itertools import combinations


def main():
    bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    bill_amt = 1
    while bill_amt <= len(bills):
        combos = combinations(bills, bill_amt)
        combo_set = set(filter(lambda combo: sum(combo) == 100, combos))
        if len(combo_set) > 0:
            print("with {} bills: {}".format(bill_amt, combo_set))
        bill_amt += 1


if __name__ == "__main__":
    main()
