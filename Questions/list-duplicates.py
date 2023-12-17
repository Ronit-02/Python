def duplicate(duplist):
    noduplist = []

    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
        else:
            print(element)



def main():
    data = [1, 2, 3, 4, 5, 5]
    duplicate(data)

if __name__ == '__main__':    # main function
    main()