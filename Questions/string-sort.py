def lensort(data):
    lst = sorted(data, key=len)
    return lst


def main():
    data = ["a", "abc", "ab", "b"]
    print(lensort(data))

if __name__ == '__main__':    # main function
    main()