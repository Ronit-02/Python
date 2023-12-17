def group(data, size):
    start = 0
    end = len(data)
    for i in range(start, end, size):
        print(data[i:i+size])



def main():
    data = [1,2,3,4,5,6,7,8]
    size = 2
    group(data, size)

if __name__ == '__main__':    # main function
    main()