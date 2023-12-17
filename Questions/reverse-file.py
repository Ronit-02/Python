def reverse():
    
    with open('data/data1.txt', 'r') as f:    
        data = f.read()
        print(data)
        # line = data.splitlines()        
        # line = line[::-1]
        # for lines in line:
        #     print(lines)

    f.close()


if __name__ == '__main__':
    reverse()