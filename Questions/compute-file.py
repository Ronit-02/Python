def readfile():
    with open('data/data1.txt', 'r') as f:
        data = f.read()
        
        line = data.splitlines()
        words = data.split()
        spaces = data.split(" ")

    f.close()

    print('\n Lines:', len(line), '\n Words:', len(words),
        '\n Spaces number:', len(spaces), '\n Characters:', (len(data)-len(spaces)))


if __name__ == '__main__':
    readfile()