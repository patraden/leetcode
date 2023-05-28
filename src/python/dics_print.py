def print_dicts(d, acc=""):
    if type(d) == dict:
        for key in d:
            print_dicts(d[key], acc + "." + str(key) if acc else str(key))
    else:
        print(acc + "." + str(d))


def main():
    test1 = {"a": {"b": {"c": 1}, "d": 2}}  # "a.b.c.1", "a.d.2"
    test2 = {"a": {"b": {"c": 1}, "d": {"e": 2}}, "f": 3}  # "a.b.c.1", "a.d.e.2", "f.3"
    test3 = {"a": 1, "b": 2, "c": 3}

    print_dicts(test1)
    print("=" * 10)
    print_dicts(test2)
    print("=" * 10)
    print_dicts(test3)


if __name__ == "__main__":
    main()
