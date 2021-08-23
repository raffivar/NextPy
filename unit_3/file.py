def read_file(file_name):
    res = "__CONTENT_START__\n"
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        res += "__NO_SUCH_FILE__\n"
    else:
        res += f.read() + "\n"
        f.close()
    finally:
        res += "__CONTENT_END__"
    return res


def main():
    print(read_file("one_lined_ile.txt"))


if __name__ == "__main__":
    main()
